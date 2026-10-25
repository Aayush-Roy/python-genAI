from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street:str
    postal_code:int
    city:str

class User(BaseModel):
    name:str
    phone:int
    address:Address

address = Address(
    street="123 something",
    postal_code=123,
    city="Delhi"
)

user = User(
    name="Aayush",
    phone=123,
    address = address
)

print(user)