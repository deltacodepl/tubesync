from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from tubesync.db.dao.channel_dao import ChannelDAO
from tubesync.db.models.channel import ChannelModel
from tubesync.web.api.dummy.schema import ChannelModelDTO, ChannelModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[ChannelModelDTO])
async def get_channels(
    limit: int = 10,
    offset: int = 0,
    dummy_dao: ChannelDAO = Depends(),
) -> List[ChannelModel]:
    """
    Retrieve all dummy objects from the database.

    :param limit: limit of dummy objects, defaults to 10.
    :param offset: offset of dummy objects, defaults to 0.
    :param dummy_dao: DAO for dummy models.
    :return: list of dummy objects from database.
    """
    return await dummy_dao.get_all_channels(limit=limit, offset=offset)


@router.put("/")
async def create_channel(
    new_channel: ChannelModelInputDTO,
    channel_dao: ChannelDAO = Depends(),
) -> None:
    """
    Creates dummy model in the database.

    :param new_channel: new dummy model item.
    :param channel_dao: DAO for dummy models.
    """
    await channel_dao.create_channel(name=new_channel.name,
                                     channel_id=new_channel.channel_id)
