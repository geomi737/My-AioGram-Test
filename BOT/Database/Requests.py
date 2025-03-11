from sqlalchemy import Insert, Select, Update, Delete
from Database.models import async_session,User

#Реквест для базы данных записать пользователя при использовании /start
async def initialize_user(tg_idF,usernameF):
    async with async_session() as session:
        user = await session.scalar(Select(User).where(User.tg_id == tg_idF))

        if user is None:
            new_user = User(
               tg_id=tg_idF,
                username=usernameF,
                message_counter = 0
            )
            session.add(new_user)
        if usernameF != user.username:
            await session.execute(
                Update(User)
                .where(User.tg_id == tg_idF)
                .values(username=usernameF)
            )
        await session.commit()


#Счет сообщений
async def message_increment(tg_idF):
    async with async_session() as session:
        await session.execute(
            Update(User)
            .where(User.tg_id == tg_idF)
            .values(message_counter=User.message_counter + 1)
        )
        await session.commit()   
 
#Выдача информации
async def profile_info(tg_idF):
    async with async_session() as session:
        stmt = await session.scalar(Select(User).where(tg_idF == User.tg_id))
        if stmt is not None:
            return stmt
        else:
            return "error"
        