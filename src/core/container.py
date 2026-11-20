from dishka import AsyncContainer, make_async_container

from src.backend.download.di import DownloadProvider
from src.platforms.youtube.di import YoutubeProvider


def get_container() -> AsyncContainer:
    return make_async_container(
        DownloadProvider(),
        YoutubeProvider(),
    )
