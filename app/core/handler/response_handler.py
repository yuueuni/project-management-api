from typing import Any

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


def format_response(status: int, content: dict):
    """
    JSON 응답 형식
    """
    content["status"] = status
    return JSONResponse(
        status_code=status,
        content=content
    )


def success_response(data: Any = None, status: int = 200, message: str = None):
    """
    정상 응답 형식
    - data: 응답 데이터
    - status: HTTP 상태 코드
    - message: 성공 메시지
    - result: 성공 여부
    """
    if isinstance(data, BaseModel) or isinstance(data, list):
        data = jsonable_encoder(data)
    return format_response(
        status=status,
        content={
            "data": data or {},
            "status": status,
            "message": message,
            "result": True
        }
    )

def error_response(error: str, details: str, status: int):
    """
    실패 응답 형식
    - error: 에러 요약
    - details: 에러 상세
    """
    return format_response(
        status=status,
        content={
            "error": error,
            "details": details
        }
    )
