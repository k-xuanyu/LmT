from LmT.app import main
from pydantic import BaseModel  
from fastapi import FastAPI


app = FastAPI()


class use(BaseModel):     #定义ues类用于存储 使用主程序的相关信息
    model: str
    info: str


class config(BaseModel):   #定义config类型 储存 config api 的信息
    model: str
    info: str
    llm_api: str
    tokens: str = None
    DB_api: str
    


# 创建主路由
@app.post("/")
def create_item(item: use):
   
   r = main(item.model, item.info)

   return r 

# 创建文件配置路由
@app.put("/put/")
def config_item(item: config):

     return "此功能暂不开放"


