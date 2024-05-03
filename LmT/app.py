from LmT.llm.llm import LLM

# 入口函数

def main(model, info):

    llm = LLM()

    if model == "think":
        r = llm.post(info)

    elif model == "learning":
        r = print(info)

    else:
        r = print("erro , please use the true Argument")

    return r 

