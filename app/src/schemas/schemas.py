from pydantic import Field,BaseModel
class LoginModel(BaseModel):
    user_nick:str = Field(min_length=1)
    user_password:str = Field(min_length=3)

