from pydantic import BaseModel, computed_field

class Patient(BaseModel):
    name:str
    age:int
    height:int
    weight:int
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


p1 = Patient(
    name='aayush', age=22, height=20, weight=74 
)

print(p1, p1.calculate_bmi)