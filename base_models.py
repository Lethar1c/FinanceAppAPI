from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str


class SetConfig(BaseModel):
    user_id: int
    language: str
    theme: str


class SetLanguage(BaseModel):
    user_id: int
    language: str


class SetTheme(BaseModel):
    user_id: int
    theme: str


class GetConfig(BaseModel):
    user_id: int
