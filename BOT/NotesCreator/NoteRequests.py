from sqlalchemy import Insert, Select, Update, Delete
from Database.models import async_session,User,Subscription,Notes

async def create_note_request(tg_idF,note):
    async with async_session() as session:
        stmt = await session.scalar(Select(User).where(User.tg_id == tg_idF))
        