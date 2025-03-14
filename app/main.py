from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.handler.exception_handler import CustomException, custom_exception_handler
from app.middlewares.jwt_auth_middleware import JWTAuthMiddleware
from app.middlewares.permission_middleware import PermissionMiddleware
from app.routers import v1 as v1_router

app = FastAPI(
    title="Project Management API",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(JWTAuthMiddleware)
app.add_middleware(PermissionMiddleware)

app.add_exception_handler(CustomException, custom_exception_handler)

app.include_router(v1_router.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}

