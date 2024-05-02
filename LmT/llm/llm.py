from configparser import ConfigParser
from post import *

config = ConfigParser()


class LLM:

    def __init__(self) :   # 读取配置文件

        config.read('../conifg/LmT.ini')
        self.url = config.get('llm', 'font')
        self.name = config.get('llm', 'name')
        self.tokens = config.get('llm', 'tokens') 
        self.kind = config.get('llm', 'kind') 


    def post(self, prompt) :  # 发送 post 请求
        if self.kind == "llama":
            print(Ollama(self.url, self.name, prompt))
        
        elif self.kind == "gpt":
            pass
        else:
            pass



        