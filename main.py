import asyncio
from pprint import pprint

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.backend.download.router import router as download_router
from src.backend.settings import get_backend_settings

from dishka.integrations.fastapi import setup_dishka

from core.container import get_container
from src.platforms.youtube.service import YoutubeService


async def backend():
    settings = get_backend_settings()
    app = FastAPI(title="MediaDownloader", version="0.0.1")
    setup_dishka(container=get_container(), app=app)

    app.include_router(router=download_router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    url = "https://www.youtube.com/shorts/fLmpk5CcuHc"

    res = await YoutubeService().get_post_info(url=url)

    pprint(res.model_dump(mode="json"))



# asyncio.run(main())
if __name__ == '__main__':
    url = "https://www.youtube.com/shorts/fLmpk5CcuHc"
    asyncio.run(backend())
