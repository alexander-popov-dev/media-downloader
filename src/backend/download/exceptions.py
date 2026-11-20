class BaseDownloadError(BaseException):
    pass

class PlatformNotSupported(BaseDownloadError):
    pass