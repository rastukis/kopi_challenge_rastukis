import os
import requests

from fastapi import FastAPI, Depends

from schemas import ConversationSchema
from services import get_or_create_conversation, add_and_get_last_messages
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session

app = FastAPI()

app.title = "Kopi Challenge - Rastukis"
app.version = "1.0.0"

OLLAMA_API = os.getenv("LLM_URL")
MODEL = os.getenv("LLM_MODEL")


@app.get("/")
def home():
    return {"message": "OK"}


@app.post("/debate-chatbot")
async def debate_chatbot(conversation: ConversationSchema, session: AsyncSession = Depends(get_session)):
    conversation_id = await get_or_create_conversation(
        conversation_id=conversation.conversation_id,
        title=conversation.message,
        session=session
    )

    last_messages = await add_and_get_last_messages(
        session=session,
        role="user",
        message=conversation.message,
        conversation_id=conversation_id
    )

    payload = {"model": MODEL, "messages": last_messages[::-1], "stream": False}

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code != 200:
        return {"error": "Error with Ollama API"}

    data = response.json()

    last_messages = await add_and_get_last_messages(
        session=session,
        role="assistant",
        message=data["message"]["content"],
        conversation_id=conversation_id
    )

    return {
        "conversation_id": conversation_id,
        "message": last_messages[::-1]
    }

