from src.backend.download.exceptions import PlatformNotSupported
from src.backend.download.schemas import DownloadRequest, DownloadResponse
from src.platforms.youtube.service import YoutubeService


class DownloadService:
    def __init__(
            self,
            youtube_service: YoutubeService
    ) -> None:
        self._youtube_service = youtube_service

    async def get_download_url(self, request: DownloadRequest) -> DownloadResponse:
        if self._youtube_service.PLATFORM in request.url:
            result = await self._youtube_service.get_post_info(url=request.url)
            return DownloadResponse(
                url=result.url,
                title=result.title,
            )
        else:
            raise PlatformNotSupported("Not supported platform")
