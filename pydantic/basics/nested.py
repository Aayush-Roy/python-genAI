from pydantic import BaseModel

class Adress(BaseModel):
    city:str
    street:str
    pin:str

class Patient(BaseModel):
    name:str
    age:int
    address:Adress

p1 = Patient(
    name='Aayush', age=22, address={
        'city':'delhi',
        'pin':'123',
        'street':'gali'
    }
)

print(p1)