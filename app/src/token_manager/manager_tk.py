from app.src.servises import cle,tkm,LogsDB
from authx import AuthX
from typing import Optional,Annotated
from fastapi import Response,Form,status
from fastapi.responses import JSONResponse
from app.src.schemas import LoginModel
from app.src.routers.depends import DepDB
from app.src.models import Users
from sqlalchemy import select

def create_login_token(
                       loginForm: Optional[Annotated[LoginModel, Form()]] = None,
                       response: Optional[Response] = None,
                       depDB: Optional[DepDB] = None):
    try:
        token = secret.create_access_token(uid=f"{loginForm.user_nick}", data={"user_nick": loginForm.user_nick,
                                                                               "auth_status": True})
        stmt = select(Users.password).where(Users.name == loginForm.user_nick)
        res = depDB.execute(stmt)
        depDB.commit()

        if res.scalar() == loginForm.user_password:
            response.set_cookie(key="user_uid",
                                value=token,
                                httponly=True,
                                secure=False)

            return {"auth_status": "true",
                    "name": loginForm.user_nick}

        else:
            LogsDB.insert_loging(db=depDB, who_load="guest_not_register", log_status="ERROR",
                                 value_log=f"Кто пытался авторизоваться")
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                                content="Введен неправильный логин или пароль.")

    except Exception as e:
        LogsDB.insert_loging(db=depDB, who_load="guest_not_register", log_status="ERROR",
                             value_log=str(e))
        return {"error": e}



conf_params = cle.load_config(env_file_name="token.env",
                              from_custom_env=True,
                              varibals_for_load=["secret_key","accsess_token_exp"])

params = tkm.load_token_params(secret_key=conf_params["secret_key"],
                      accsess_token_exp=int(conf_params["accsess_token_exp"]),
                      cookie_httponly=True,
                      cookie_secure=False)

secret = AuthX(conf_params)



