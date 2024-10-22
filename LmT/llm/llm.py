from configparser import ConfigParser
from LmT.llm.post import *

config = ConfigParser()


class LLM:

    def __init__(self) :   # 读取配置文件

        config.read('/home/k/project/LmT/LmT/LmT/config/LmT.ini')
        self.url = config.get('llm', 'url')
        self.name = config.get('llm', 'name')
        self.tokens = config.get('llm', 'tokens') 
        self.kind = config.get('llm', 'kind') 


    def post(self, prompt) :  # 发送 post 请求
        
        if self.kind == "llama":
            r = Ollama(self.url, self.name, prompt)
            return r
        
        elif self.kind == "gpt":
            return "此功能暂未开放请使用 Ollama"
        
        else:
            return "你未进行该框架的 post 初始化"



