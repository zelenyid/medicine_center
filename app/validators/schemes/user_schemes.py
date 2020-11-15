from pydantic import BaseModel


class UserScheme(BaseModel):
    email: str
    password: str
