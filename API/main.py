import sys
sys.path.append(r"../")
from LmT.app import main
from pydantic import BaseModel  
from fastapi import FastAPI
from LmT.config.config import Config


app = FastAPI()


class use(BaseModel):     #
    model: str
    info: str
    llm_api: str
    tokens: str = None
    DB_api: str

class config(BaseModel):
    model: str
    info: str
    llm_api: str
    tokens: str = None
    DB_api: str
    


# 创建主路由
@app.post("/")
def create_item(item: use):
   r =  main(item.model, item.info, item.llm_api, item.tokens, item.DB_api)

   return r 


@app.put("/")
def config_item(item: config):

     return "此功能暂不开放"