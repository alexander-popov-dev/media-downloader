from dishka import AsyncContainer, make_async_container

from backend.download.di import DownloadProvider
from platforms.youtube.di import YoutubeProvider


def get_container() -> AsyncContainer:
    return make_async_container(
        DownloadProvider(),
        YoutubeProvider(),
    )
