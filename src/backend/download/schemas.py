from pydantic import BaseModel


class DownloadRequest(BaseModel):
    url: str

class DownloadResponse(BaseModel):
    url: str
    title: str