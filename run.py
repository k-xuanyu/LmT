import uvicorn

from LmT.app import app

# 运行项目：开发模式

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.3.55", port=8000)