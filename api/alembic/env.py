import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

from src import models
from src.settings import settings


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

models.load()

target_metadata = models.Base.metadata


def do_run_migrations(connection):
    context.configure(
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    connectible = create_async_engine(url=settings.db_url, future=True)

    async with connectible.connect() as connection:
        await connection.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())
