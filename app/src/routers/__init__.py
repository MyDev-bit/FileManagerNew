from fastapi import APIRouter
from app.src.routers.router_1 import loginRouter


MainRouter = APIRouter()

MainRouter.include_router(loginRouter)