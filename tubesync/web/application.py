from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from tubesync.web.api.router import api_router
from tubesync.web.lifetime import register_shutdown_event, register_startup_event


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="tubesync",
        version=metadata.version("tubesync"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    @app.on_event("startup")
    def test_print():
        """
        Test print
        """
        print("Hello world")

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
