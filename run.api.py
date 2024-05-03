# 用 api 使用本项目

import uvicorn
from API.main import app

# 运行项目

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.3.55", port=8000)