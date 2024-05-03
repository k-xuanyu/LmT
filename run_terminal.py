# 用终端使用本项目
from LmT.app import main



if __name__ == "__main__":

    model = input("Please choose the model that you want ：[think] or [learning]")
    info = input("Please input the information")

    r = main(model, info)

    print(r)