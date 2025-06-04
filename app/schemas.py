from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class TransactionCreate(BaseModel):
    type: str
    category: str
    amount: float

class TransactionOut(TransactionCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
