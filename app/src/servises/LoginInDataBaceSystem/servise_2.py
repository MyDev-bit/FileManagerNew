from typing import Optional
from app.src.models import Logging
from sqlalchemy import insert
from app.src.routers.depends import DepDB


class LoginInDataBaceSystem:
    def insert_loging(self = None,
                   db:Optional[DepDB] = None,
                   who_load:Optional[str] = None,
                   value_log:Optional[str] = None,
                    log_status:Optional[str] = "INFO"):
        stmt = insert(Logging).values({"log_id":id(value_log),
                                       "log_status":log_status,
                                       "who_load_value":who_load,
                                       "log_value":value_log})

        db.execute(stmt)
        db.commit()
