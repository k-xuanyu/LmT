import sys
sys.path.append(r"../")
from LmT.app import main
from pydantic import BaseModel  
from fastapi import FastAPI


app = FastAPI()


class Item(BaseModel):
    model: str
    info: str
    llm_api: str
    tokens: str = None
    DB_api: str
    


# 创建主路由
@app.post("/")
def create_item(item: Item):
   r =  main(item.model, item.info, item.llm_api, item.tokens, item.DB_api)

   return r 

