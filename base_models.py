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


class CreateNewAccount(BaseModel):
    user_id: int
    name: str
    description: str


class AddNewIncome(BaseModel):
    account_id: int
    sum: float
    name: str
    description: str
    category: str


class AddNewOutcome(BaseModel):
    account_id: int
    sum: float
    name: str
    description: str
    category: str


class AddNewTransaction(BaseModel):
    from_account_id: int
    to_account_id: int
    sum: float
    description: str
