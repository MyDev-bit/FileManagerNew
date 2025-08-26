from fastapi import APIRouter, UploadFile,Request,HTTPException,status
from fastapi.responses import FileResponse ,JSONResponse
from app.src.servises.servises import TokenManager,LogsDB,ClientFileManager
from pathlib import Path
from sqlalchemy import delete
from app.src.models import Files
from app.src.routers.depends import DepDB

fileManagerRouter =  APIRouter(tags=["Работа с файлами"])
cfm = ClientFileManager()
tkm = TokenManager()

@fileManagerRouter.post("/upload_file")
def upload_file(upload:UploadFile
                ,db:DepDB,request:Request):
    token = tkm.get_decode_token_values(cookie_name='user_uid',
                                        request=request)
    name = token["user_nick"]
    if token["auth_status"]:
            status = cfm.load_files(upload, db,user_nick=str(token["user_nick"]))
            LogsDB.insert_loging(db=db, who_load=name, log_status="INFO",
                                 value_log=f"Пользователь: {name} загрузил файл.Название файла:{upload.filename}.")
            return status
    else:
            LogsDB.insert_loging(db=db, who_load=name, log_status="ERROR",
                             value_log=f"Кто пытался сделать запрос на загрузку файла")
            raise HTTPException(status_code=403,detail="Нет доступа")




@fileManagerRouter.get("/all_files")
def all_files(request:Request,db:DepDB):

    token = tkm.get_decode_token_values(cookie_name='user_uid',
                                        request=request)

    name = token["user_nick"]
    if token["auth_status"]:
        files = cfm.all_files()
        LogsDB.insert_loging(db=db, who_load=name, log_status="INFO",
                             value_log=f"Пользователь: {name} посмотрел список всех файлов.")
        return files
    else:

        raise HTTPException(status_code=403,
                            detail="У вас нет доступа")




@fileManagerRouter.get("/send_file")
def send_file(request:Request,
              file_name:str,db:DepDB):
    token = tkm.get_decode_token_values(cookie_name='user_uid',
                                        request=request)
    name = token["user_nick"]
    if token["auth_status"]:
        try:
            file_path = Path("../../ClientFiles") / file_name
            LogsDB.insert_loging(db=db, who_load=name, log_status="INFO",
                                 value_log=f"Пользователь: {name} скачал файл.Название файла:{file_name}")
            return FileResponse(file_path,filename=file_name)
        except FileNotFoundError:
            LogsDB.insert_loging(db=db, who_load=name, log_status="ERROR",
                                 value_log=f"Пользователь: {name} пытался скачать несуществующий файл.Название файла {file_name}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Нет такого файла")


    else:
        LogsDB.insert_loging(db=db, who_load=name, log_status="ERROR",
                             value_log=f"Кто пытался сделать запрос на скачивание файла")
        raise HTTPException(status_code=403,
                            detail="У вас нет доступа")





@fileManagerRouter.delete('/delete_file')
def delete_file(request:Request,file_name:str,
                db:DepDB):
    token = tkm.get_decode_token_values(cookie_name='user_uid',
                                        request=request)

    file_path = Path("../../ClientFiles") / file_name
    name = token["user_nick"]
    if token["auth_status"]:
        try:
            file_path.unlink()
            stmt = delete(Files).where(Files.file_name == file_name)
            db.execute(stmt)
            db.commit()
            LogsDB.insert_loging(db=db, who_load=name, log_status="ERROR",
                                 value_log=f"Пользователь: {name} удалил файл.Название файла {file_name}")
            return JSONResponse(status_code=status.HTTP_200_OK,content="Файл удален")
        except FileNotFoundError:
            LogsDB.insert_loging(db=db, who_load=name, log_status="ERROR",
                                 value_log=f"Пользователь: {name} пытался удалить несуществующий файл.Название файла {file_name}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Файл не найден")

    else:
        raise HTTPException(status_code=403,
                            detail="У вас нет доступа")
