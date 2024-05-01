import sys
sys.path.append(r"../")
from LmT.app import main
from pydantic import BaseModel  
from fastapi import FastAPI


app = FastAPI()


class Item(BaseModel):
    model: str
    info: str


# 创建主路由
@app.post("/")
def create_item(item: Item):
   r =  main(item.model, item.info)

   return r 

