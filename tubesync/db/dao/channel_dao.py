from typing import List, Optional

from fastapi import Depends
from psycopg.rows import class_row
from psycopg_pool import AsyncConnectionPool

from tubesync.db.dependencies import get_db_pool
from tubesync.db.models.channels_model import ChannelModel


class ChannelDAO:
    """Class for accessing channels table."""

    def __init__(
        self,
        db_pool: AsyncConnectionPool = Depends(get_db_pool),
    ):
        self.db_pool = db_pool

    async def create_channel_model(self, name: str, channel_id: str) -> None:
        """
        Creates new channel in a database.

        :param name: name of a channel.
        :param channel_id: id of the channel.
        """
        async with self.db_pool.connection() as connection:
            async with connection.cursor(binary=True) as cur:
                await cur.execute(
                    "INSERT INTO channels (name) VALUES (%(name)s);",
                    params={
                        "name": name,
                        "channel_id": channel_id,
                    },
                )

    async def get_all_channels(self, limit: int, offset: int) -> List[ChannelModel]:
        """
        Get all channels models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        async with self.db_pool.connection() as connection:
            async with connection.cursor(
                binary=True,
                row_factory=class_row(ChannelModel),
            ) as cur:
                res = await cur.execute(
                    "SELECT id, name FROM channels LIMIT %(limit)s OFFSET %(offset)s;",
                    params={
                        "limit": limit,
                        "offset": offset,
                    },
                )
                return await res.fetchall()

    async def filter(
        self,
        name: Optional[str] = None,
    ) -> List[ChannelModel]:
        """
        Get specific channel model.

        :param name: name of channels instance.
        :return: channels models.
        """
        async with self.db_pool.connection() as connection:
            async with connection.cursor(
                binary=True,
                row_factory=class_row(ChannelModel),
            ) as cur:
                if name is not None:
                    res = await cur.execute(
                        "SELECT id, name FROM channels WHERE name=%(name)s;",
                        params={
                            "name": name,
                        },
                    )
                else:
                    res = await cur.execute("SELECT id, name FROM channels;")
                return await res.fetchall()
