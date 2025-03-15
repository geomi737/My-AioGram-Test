from logging.config import fileConfig

from sqlalchemy.ext.asyncio import async_engine_from_config, AsyncEngine
from sqlalchemy import pool
from alembic import context
import asyncio

from BOT.Database.models import Base

# Alembic конфиг
config = context.config

# Логирование
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Твой target_metadata (если у тебя есть модели, добавь их сюда)
target_metadata = Base.metadata

# Функция для оффлайн-миграции
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Функция для онлайн-миграции
async def run_migrations_online() -> None:
    engine: AsyncEngine = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with engine.begin() as connection:
        await connection.run_sync(do_run_migrations)

# Функция, которая будет запущена внутри `run_sync`
def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

# Выбор режима
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
