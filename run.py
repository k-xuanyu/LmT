import uvicorn

import LmT.app
# 运行项目

if __name__ == "__main__":
    uvicorn.run(app="run:app", port=8000)