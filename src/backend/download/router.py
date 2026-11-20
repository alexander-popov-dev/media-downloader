from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette import status

from src.backend.download.schemas import DownloadResponse, DownloadRequest
from src.backend.download.service import DownloadService
from src.backend.settings import get_backend_settings

router = APIRouter(prefix="/download", tags=["download"])

settings = get_backend_settings()


@router.get(
    path="/",
    response_model=DownloadResponse,
    status_code=status.HTTP_200_OK,
)
@inject
async def get_download_url(
        url: str,
        service: Annotated[DownloadService, FromDishka()],
) -> DownloadResponse:

    request = DownloadRequest(url=url)
    return await service.get_download_url(request=request)
