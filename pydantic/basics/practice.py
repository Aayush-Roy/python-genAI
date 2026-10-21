from pydantic import BaseModel, Field, field_validators

class Student(BaseModel):
    name:str = Field(
        min_length=3
    )
    age:int
    @field_validators('age')
    def chec_len(cls,v):
        if v.age<18:
            raise ValueError("Age should begt 18")
        return v
    email:str
    marks:float
    @field_validators('marks')
    def check_marks(cls,v):
        if ((v.marks>0) && (v.marks<100)):
            raise ValueError("")
        return v