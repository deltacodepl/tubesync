from fastapi.routing import APIRouter

from tubesync.web.api import channel, echo, monitoring, redis

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(channel.router, prefix="/channel", tags=["channel"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
