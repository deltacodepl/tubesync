from typing import Any
from psycopg import AsyncConnection


async def create_tables(connection: AsyncConnection[Any]) -> None:
    await connection.execute(
        "CREATE TABLE IF NOT EXISTS channels"
        "(id serial PRIMARY KEY, name VARCHAR(200) NOT NULL,"
        "channel_id VARCHAR(200) NOT NULL); "
    )

