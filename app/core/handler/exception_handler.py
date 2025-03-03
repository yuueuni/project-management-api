from fastapi import HTTPException, Request

from app.core.handler.response_handler import error_response


class CustomException(HTTPException):
    def __init__(self, error: str, details: str = None, status: int = 400):
        """
        - error: 오류 요약
        - details: 오류에 대한 추가 세부 정보
        - code: HTTP 상태 코드
        """
        self.error = error
        self.details = details
        self.status = status
        super().__init__(status_code=status, detail=error)

async def custom_exception_handler(request: Request, exc: CustomException):
    """
    Custom error handler
    """
    return error_response(
        error=exc.error,
        details=exc.details,
        status=exc.status
    )
