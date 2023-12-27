from typing import Optional
from pydantic import BaseModel

# Pydantic models for MongoDB

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str

class DailyReportCreate(BaseModel):
    client_code: str
    first_name: str
    last_name: str
    type: str
    weight: float
    payment_method: str

class StatusReportCreate(BaseModel):
    branch: str
    washer: int
    dryer: int
    fold: int
    backlog: int

class CycleCountCreate(BaseModel):
    image_url: str

class ReceivablesCheck(BaseModel):
    client_code: str

class TransferLaundryUpdate(BaseModel):
    client_code: str
    branch: str