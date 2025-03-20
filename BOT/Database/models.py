from sqlalchemy.ext.asyncio import create_async_engine,AsyncAttrs,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import BigInteger,ForeignKey,Date
import asyncio

import datetime

engine = create_async_engine(
    url="sqlite+aiosqlite:///db.sqlite3",
)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase,AsyncAttrs):
    pass

class User(Base):
    __tablename__ = 'Users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(nullable=True)
    message_counter: Mapped[int]
    

class Subscription(Base):
    __tablename__ = 'Subscriptions'
    
    user_id: Mapped[int] = mapped_column(ForeignKey('Users.id'),primary_key=True)
    subscription_activity: Mapped[bool] = mapped_column(default=False)
    subscription_date = mapped_column(Date,nullable=True)
    subscription_days: Mapped[int] = mapped_column(nullable=True)
    
class Notes(Base):
    __tablename__ = 'Notes'
    
    user_id: Mapped[int] = mapped_column(ForeignKey('Users.id'),primary_key=True)
    note: Mapped[dict] = mapped_column()
    
async def create_new_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)