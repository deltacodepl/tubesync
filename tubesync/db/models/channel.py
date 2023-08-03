from pydantic import BaseModel


class ChannelModel(BaseModel):
    """Channel model for database."""
    id: int
    name: str
    subscribed: bool
