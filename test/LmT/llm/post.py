# 这里的可以自己添加修改，目前只支持 Ollama 框架 和 gpt

import json
import requests


def Gpt():
    pass


def Ollama(url, name, prompt):
    
    post_json = json.dumps(
        {
        "model": name,
        "prompt": prompt,
        "stream": false ,# type: ignore
        "format": "json"
        }
        )
    
    r = requests.post(url, data=post_json)
    
    return r
