from typing import Optional

from pydantic import BaseModel


class PhoneRequest(BaseModel):
    phone: str
    description:str



class OrderList(BaseModel):
    phone: str
    description:str
    status : Optional[str] = None

    class Config:
        from_attributes = True