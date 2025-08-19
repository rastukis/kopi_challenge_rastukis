from sqlalchemy.ext.asyncio import AsyncSession

from models import Conversation, Message


async def create_conversation(title: str, session: AsyncSession):
    conversation = Conversation(
        title=title
    )
    session.add(conversation)
    await session.commit()
    await session.refresh(conversation)
    return conversation


async def get_or_create_conversation(session: AsyncSession, conversation_id=None, title=None, ):
    if conversation_id:
        result = await session.execute(
            Conversation.__table__.select().where(Conversation.id == conversation_id)
        )
        conversation = result.scalars().one()
        if not conversation:
            conversation = await create_conversation(title=title, session=session)
            return conversation.id
        return conversation
    conversation = await create_conversation(title=title, session=session)
    return conversation.id


async def add_new_message(session: AsyncSession, role: str, message: str, conversation_id):
    new_message = Message(
        role=role,
        message=message,
        conversation_id=conversation_id
    )
    session.add(new_message)
    await session.commit()
    await session.refresh(new_message)
    return new_message


async def get_last_messages_by_conversation_id(conversation_id, session: AsyncSession):
    last_messages = await session.execute(
        Message.__table__.select()
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.desc())
        .limit(5)
    )
    return list(last_messages)


async def add_and_get_last_messages(session: AsyncSession, role: str, message: str, conversation_id):
    new_message = await add_new_message(
        session=session,
        role=role,
        message=message,
        conversation_id=conversation_id
    )

    last_messages = await get_last_messages_by_conversation_id(
        conversation_id=conversation_id,
        session=session
    )

    return [{"role": item.role, "content": item.message} for item in last_messages]



