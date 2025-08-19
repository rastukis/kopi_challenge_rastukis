from pydantic import BaseModel, UUID4
from typing import Optional


class ConversationSchema(BaseModel):
    conversation_id: Optional[UUID4] = None
    message: str
