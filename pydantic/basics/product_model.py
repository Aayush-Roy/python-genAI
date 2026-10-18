from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True

product_one = Product(id=101, name="iphone", price=1200.99, in_stock=True)
product_two = Product(id=102, name="keyborad", price=350.67)
product_three = Product(name="samsung")
