from typing import Optional
from fastapi import UploadFile
from pathlib import Path
from sqlalchemy import insert
from app.src.models import Files
from fastapi import status
from fastapi.responses import JSONResponse
from app.src.routers.depends import DepDB
from app.src.servises.LoginInDataBaceSystem import LogsDB

import os

class ClientFileManager:
    def load_files(self:Optional[str] = None,
                   upload:Optional[UploadFile] = None,
                   db:Optional[DepDB] = None,
                   user_nick:Optional[str] = None):
        try:
            file_name = upload.filename
            file_extension = list(os.path.splitext(file_name))
            file_patch = Path(f"../../../ClientFiles") / file_name
            with file_patch.open("wb") as fl:
                    fl.write(upload.file.read())

                    stmt = insert(Files).values({"file_id": id(file_name), "file_name": file_name,
                                                 "file_extension":str(file_extension[1]),"user_load":user_nick})
                    db.execute(stmt)
                    db.commit()

                    return JSONResponse(status_code=status.HTTP_200_OK,content="Файлы загружены")
        except FileNotFoundError:
            LogsDB.insert_loging(db=db, who_load="guest_not_register", log_status="ERROR",
                                 value_log=f"{user_nick} пытался загрузить несуществующий файл.Название файла:{user_nick}")
            return {
            "status_load":"false"
            }


    def all_files(self:Optional[None] = None,
                  ):
        files = []
        files_dict = {}
        patch = Path("../../../ClientFiles/")


        for file in patch.iterdir():
            files.append(file.name)

        for z in files:
            files_dict[f"file_{id(z)}"] = z

        return files_dict





