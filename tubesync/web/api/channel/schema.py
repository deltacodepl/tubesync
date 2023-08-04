from pydantic import BaseModel, ConfigDict


class ChannelModelDTO(BaseModel):
    """
    DTO for channel model.

    It returned when accessing channel from the API.
    """
    id: int
    name: str
    channel_id: str
    model_config = ConfigDict(from_attributes=True)


class ChannelModelInputDTO(BaseModel):
    """DTO for creating new channel model."""
    name: str
    channel_id: str
