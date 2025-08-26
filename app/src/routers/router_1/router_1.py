from fastapi import APIRouter,Response,Request,status,HTTPException,Form
from app.src.routers.depends import DepDB
from app.src.schemas import LoginModel
from typing import Annotated
from app.src.servises import TokenManager,LogsDB


loginRouter = APIRouter(tags=["Меню пользователя"])

tkm = TokenManager()
@loginRouter.post('/logout')
def logout(response:Response,
           request:Request,
           db:DepDB):
    token = tkm.get_decode_token_values(cookie_name='user_uid',
                                        request=request)
    name = token["user_nick"]
    if token["auth_status"]:
        response.delete_cookie(key="user_uid",path="/")
        LogsDB.insert_loging(db=db, who_load=name, log_status="INFO",
                             value_log=f"Пользователь: {name} вышел из своего аккаунта.")
        return {"logout_status":"true"}

    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Вы не авторизованы')




@loginRouter.post('/login')
def login(loginForm:Annotated[LoginModel,Form()],
          db:DepDB,response:Response):
    login_status = tkm.create_login_token(loginForm=loginForm,
                                          depDB=db,
                                          response=response)

    LogsDB.insert_loging(db=db,who_load=loginForm.user_nick,log_status="INFO",value_log=f"Пользователь: {loginForm.user_nick} вошел в свой аккаунт.")
    return login_status
