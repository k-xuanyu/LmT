import uvicorn

from API.main import app
from test.test_main import TestMain

# 运行项目：开发模式

if __name__ == "__main__":
    # uvicorn.run(app, host="192.168.3.55", port=8000)
    TestMain()