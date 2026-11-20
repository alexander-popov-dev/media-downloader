from dishka import Provider, provide, Scope

from backend.download.service import DownloadService
from platforms.youtube.service import YoutubeService


class DownloadProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_download_service(
            self,
            youtube_service: YoutubeService,
    ) -> DownloadService:
        return DownloadService(
            youtube_service=youtube_service
        )
