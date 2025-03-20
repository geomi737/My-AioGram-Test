from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from Database.models import Subscription
from Database.models import async_session
from sqlalchemy import select, update

scheduler = AsyncIOScheduler()

async def check_sub():
    async with async_session() as session:
        stmt = select(Subscription).where(Subscription.subscription_activity == True)
        result = await session.execute(stmt)
        subscriptions = result.scalars().all()
        
        now = datetime.now().date()
        
        for sub in subscriptions:
            if sub.subscription_date and sub.subscription_date < now:
                print(f"Subscription {sub.user_id} has expired")
                
                sub.subscription_activity = False
                sub.subscription_date = None
                sub.subscription_days = None
                
                await session.commit()
                
scheduler.add_job(check_sub, 'interval', minutes=1)