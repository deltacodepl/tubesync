import uuid

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from psycopg_pool import AsyncConnectionPool
from starlette import status

from tubesync.db.dao.channel_dao import ChannelDAO


@pytest.mark.anyio
async def test_creation(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbpool: AsyncConnectionPool,
) -> None:
    """Tests channel instance creation."""
    url = fastapi_app.url_path_for("create_channel")
    test_name = uuid.uuid4().hex
    response = await client.put(
        url,
        json={
            "name": test_name,
            "channel_id": test_name,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    dao = ChannelDAO(dbpool)
    instances = await dao.filter(name=test_name)
    assert instances[0].name == test_name


@pytest.mark.anyio
async def test_getting(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbpool: AsyncConnectionPool,
) -> None:
    """Tests channel instance retrieval."""
    dao = ChannelDAO(dbpool)
    test_name = uuid.uuid4().hex
    await dao.create_channel(name=test_name, channel_id=test_name)
    url = fastapi_app.url_path_for("get_channels")
    response = await client.get(url)
    dummies = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(dummies) == 1
    assert dummies[0]["name"] == test_name
