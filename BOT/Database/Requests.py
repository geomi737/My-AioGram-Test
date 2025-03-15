from sqlalchemy import Insert, Select, Update, Delete
from Database.models import async_session,User,Subscription

from datetime import datetime, timedelta
import time

async def initialize_user(tg_idF,usernameF):
    async with async_session() as session:
        user = await session.scalar(Select(User).where(User.tg_id == tg_idF))

        if user is None and usernameF != "NonameHASH128125125152612":
            new_user = User(
               tg_id=tg_idF,
                username=usernameF,
                message_counter = 0
            )
            session.add(new_user)
        
        elif user is None:
            new_user = User(
               tg_id=tg_idF,
                username="Ваш username некорректен!",
                message_counter = 0
            )
            session.add(new_user)
        if usernameF != "NonameHASH128125125152612":
            if usernameF != user.username:
                await session.execute(
                    Update(User)
                    .where(User.tg_id == tg_idF)
                    .values(username=usernameF)
                )
        
        await session.commit()

        
async def message_increment(tg_idF):
    async with async_session() as session:
        await session.execute(
            Update(User)
            .where(User.tg_id == tg_idF)
            .values(message_counter=User.message_counter + 1)
        )
        await session.commit()   
    
#request can be "User Info" string,or "Sub Info" string
async def profile_info(tg_idF,request):
    async with async_session() as session:
        UserInfo = await session.scalar(Select(User).where(tg_idF == User.tg_id))
        SubInfo = await session.scalar(Select(Subscription).where(UserInfo.id == Subscription.user_id))
        if UserInfo is not None:
            if request == "User Info":
                return UserInfo
            elif request == "Sub Info":
                if SubInfo != False and SubInfo != 0 and SubInfo != None:
                    return SubInfo
                else:
                    return "Отсутствие данных!"
        else:
            return "Отсутствие данных!"
        

async def add_subscription(tg_idF, subDate):
    async with async_session() as session:
        # First, get the user
        user = await session.scalar(Select(User).where(User.tg_id == tg_idF))
        
        # Check if user exists
        if user is None:
            return "Error: Не найден пользователь"

        # Get existing subscription
        sub_user = await session.scalar(
            Select(Subscription).where(Subscription.user_id == user.id)
        )

        if sub_user is None:
            # Create new subscription
            new_sub = Subscription(
                user_id=user.id,
                subscription_date=datetime.now().date() + timedelta(days=subDate),
                subscription_activity=True,
                subscription_days=subDate
            )
            session.add(new_sub)
            await session.commit()
            return "SUCCESS!"
        else:
            # Update existing subscription
            if sub_user.subscription_activity == False:
                await session.execute(
                    Update(Subscription)
                    .where(Subscription.user_id == user.id)
                    .values(
                        subscription_date=datetime.now().date() + timedelta(days=subDate),
                        subscription_activity=True,
                        subscription_days=subDate
                    )
                )
                await session.commit()
                return "SUCCESS!"
            
            else: return "Error: Подписка уже есть"
        

async def subscription_cancel(tg_idF):
    async with async_session() as session:
        user = await session.scalar(Select(User).where(User.tg_id == tg_idF))
        
        if user is None:
            return "Error: Не найден пользователь"
        
        sub_user = await session.scalar(Select(Subscription).where(Subscription.user_id == user.id))
        if sub_user is None:
            return "Error: Не найдена подписка"
        
        if sub_user.subscription_activity == True:
            await session.execute(Update(Subscription).where(Subscription.user_id == user.id).values(subscription_activity=False,subscription_date=None,subscription_days=None))
            await session.commit()
            return "SUCCESS!"
        
        else:
            return "Error: Подписка неактивна"
        
        
    
async def renew_sub_request(tg_idF):
    async with async_session() as session:
        user = await session.scalar(Select(User).where(User.tg_id == tg_idF))
        
        if user is None:
            return "Error: Не найден пользователь"
        
        sub_user = await session.scalar(Select(Subscription).where(Subscription.user_id == user.id))
        
        if sub_user is None:
            return "Error: Не найдена подписка"
        
        if sub_user.subscription_activity == False:
            return "Error: Подписка неактвна"
        
        if sub_user.subscription_date - datetime.now().date() > timedelta(days=3):
            return "Error: Подписка активна более 3 следующих дней"
        
        else:
            await session.execute(Update(Subscription).where(Subscription.user_id == user.id).values(subscription_activity=True,subscription_date=datetime.now().date() + timedelta(days=sub_user.subscription_days),subscription_days=sub_user.subscription_days))
            await session.commit()
            return "SUCCESS!"