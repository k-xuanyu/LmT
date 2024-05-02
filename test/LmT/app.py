import sys
sys.path.append(r"../")
from LmT.llm.llm import LLM


def main(model, info):

    llm = LLM()

    if model == "thing":
        r = llm.post(info)

    elif model == "learning":
        r = print(info)

    else:
        r = print("erro , please use the true Argument")

    return r 

