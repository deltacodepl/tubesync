from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from tubesync.db.dao.channel_dao import ChannelDAO
from tubesync.db.models.dummy_model import ChannelModel
from tubesync.web.api.dummy.schema import DummyModelDTO, DummyModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[DummyModelDTO])
async def get_dummy_models(
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
async def create_dummy_model(
    new_dummy_object: DummyModelInputDTO,
    dummy_dao: ChannelDAO = Depends(),
) -> None:
    """
    Creates dummy model in the database.

    :param new_dummy_object: new dummy model item.
    :param dummy_dao: DAO for dummy models.
    """
    await dummy_dao.create_channel_model(name=new_dummy_object.name)
