from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str, int]

class BlogPost(BaseModel):
    title:str
    comment:str
    image_url:Optional[str] = None

cart1 = Cart(user_id=101,items=["soap","scrub","face_wash"], quantities={"soap":5,"scrub":10})

print(cart1)
