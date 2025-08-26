import secrets
from sqlalchemy import String
from sqlalchemy.orm import MappedAsDataclass,mapped_column,DeclarativeBase
from typing import Annotated
from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.src.routers import MainRouter
import uvicorn

app = FastAPI(title="FIleManager")






default_len = Annotated[str,mapped_column(String(200))]







app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:40"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






fileManagerRouter =  APIRouter(tags=["Работа с файлами"])




class Base(MappedAsDataclass,DeclarativeBase):
    pass


secret_id_file = secrets.token_hex(16)
secret_id_user = secrets.token_hex(5)
# файлы сделать завтра









app.include_router(MainRouter)






if __name__ == '__main__':
    uvicorn.run('app.src.api:app',reload=True)