from typing import Optional
from authx import AuthXConfig
from datetime import timedelta

from fastapi import Request,HTTPException
from jwt.exceptions import DecodeError,ExpiredSignatureError
import jwt




class TokenManager:
    """Это класс для создания и управление jwt токен.
    Через библиотеки :PyJWT,authx,dotenv"""




    def load_token_params(self:Optional[str] = None,
                              secret_key:Optional[str] = None,
                              token_location:Optional[list[str]] = ["cookies"],
                              accsess_token_exp:Optional[int] = 90,
                              refresh_token_exp:Optional[int] = 360,
                              accsess_cookie_name:Optional[str] = None,
                              refresh_cookie_name: Optional[str] = None,
                              cookie_secure:Optional[bool] = None,
                              cookie_httponly:Optional[bool] = None):

        """Эта функция устанавливает параметр для authx"""

        authxConf = AuthXConfig()
        authxConf.JWT_SECRET_KEY = secret_key
        authxConf.JWT_TOKEN_LOCATION = token_location
        authxConf.JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=accsess_token_exp)
        authxConf.JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=refresh_token_exp)
        authxConf.JWT_ACCESS_COOKIE_NAME = accsess_cookie_name
        authxConf.JWT_REFRESH_COOKIE_NAME = refresh_cookie_name
        authxConf.JWT_COOKIE_SECURE = cookie_secure
        authxConf.JWT_COOKIE_HTTP_ONLY = cookie_httponly

        return authxConf

    def decode(self = None,cookie_name: Optional[str] = None):
        """Это функция декодирует токен.
        Если честно ее можно даже не вызывать надо вызвать функцию get_decode_token_values
         Тогда выдит значение"""
        def cookie(request: Request):
            try:
                get_uid_cookies = request.cookies.get(cookie_name)
                token = jwt.decode(get_uid_cookies, "SECRET", algorithms=["HS256"])
                print(token)
                return token

            except DecodeError:
                raise HTTPException(status_code=401, detail="Вы не авторизованны")
            except ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Вы не авторизованны")

        return cookie

    def get_decode_token_values(self = None,
                                cookie_name: Optional[str] = None,
                                request: Optional[Request] = None):
        """Эта функция создана для того что бы получить значение с декодированного токена.
        Я знаю это можно было сделать и легче но я сделал так.
        В cookie_name укажите название куки
        В request укажите параметр request из функции  """
        get_token = tkm.decode(cookie_name)
        token = get_token(request=request)

        return token



tkm = TokenManager()


