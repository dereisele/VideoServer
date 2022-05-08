import logging.config

import coloredlogs
from fastapi import FastAPI
import uvicorn

from .routers import dlna
from .discovery.socket import register_ssdp
from .dependencies import get_settings

settings = get_settings()
logging.config.dictConfig(settings.logging)
# coloredlogs.install()
log = logging.getLogger(__name__)

log.debug("Creating App")
app = FastAPI()

app.include_router(dlna.router)


@app.on_event("startup")
async def on_startup() -> None:
    log.info("Starting DLNA Discovery Server")
    transport, discovery_server = await register_ssdp(settings)

    app.state.discovery_server = discovery_server


@app.on_event("shutdown")
async def on_shutdown() -> None:
    log.info("Giving Discovery Server signal to shut down")
    app.state.discovery_server.shutdown()

if __name__ == "__main__":
    uvicorn.run(app, host=settings.server_ip, port=settings.server_port)
