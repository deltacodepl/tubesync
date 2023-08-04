from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from tubesync.db.dao.channel_dao import ChannelDAO
from tubesync.db.models.channel import ChannelModel
from tubesync.web.api.channel.schema import ChannelModelDTO, ChannelModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[ChannelModelDTO])
async def get_channels(
    limit: int = 10,
    offset: int = 0,
    channel_dao: ChannelDAO = Depends(),
) -> List[ChannelModel]:
    """
    Retrieve all channel objects from the database.

    :param limit: limit of channel objects, defaults to 10.
    :param offset: offset of channel objects, defaults to 0.
    :param channel_dao: DAO for channel models.
    :return: list of channel objects from database.
    """
    return await channel_dao.get_all_channels(limit=limit, offset=offset)


@router.put("/")
async def create_channel(
    new_channel: ChannelModelInputDTO,
    channel_dao: ChannelDAO = Depends(),
) -> None:
    """
    Creates channel model in the database.

    :param new_channel: new channel model item.
    :param channel_dao: DAO for channel models.
    """
    await channel_dao.create_channel(name=new_channel.name,
                                     channel_id=new_channel.channel_id)
