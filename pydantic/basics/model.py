from pydantic import BaseModel, field_validator, Field, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name:str
    age:int
    allergies:List[str]=Field(max_length=5)
    contact_details:Dict[str,str]
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in  self.contact_details:
            raise ValueError('Patients older than 60 must have emergenct contact')
        return self

p1 = Patient(
    name='Aayush', age = 65, allergies=['dust','wind'], contact_details={
        'email':'aayush@gmail.com',
        'phone':'12345',
        'emergency':'1234567'
    }
)

print(p1)