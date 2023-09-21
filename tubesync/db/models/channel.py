from pydantic import BaseModel


class ChannelModel(BaseModel):
    """Channel model for database."""
    id: int
    name: str
    channel_id: str
    subscribed: bool
