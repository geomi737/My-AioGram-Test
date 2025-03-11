from sqlalchemy.ext.asyncio import create_async_engine,AsyncAttrs,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import BigInteger,ForeignKey
import asyncio

#Создание базы данных и таблиц
engine = create_async_engine(
    url="sqlite+aiosqlite:///db.sqlite3"
)

#Создание менеджера сессий
async_session = async_sessionmaker(engine)

#Основной класс
class Base(DeclarativeBase,AsyncAttrs):
    pass

#Наследующие классы
class User(Base):
    __tablename__ = 'Users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(nullable=True)
    message_counter: Mapped[int]

#Создание новых таблиц
async def create_new_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)