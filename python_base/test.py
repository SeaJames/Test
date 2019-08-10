# -*- coding: utf-8 -*-
"""
Author: 17161
Date: 2019/8/10
"""


def wrapper(func):
    print("welcome to wrapper haha")

    def do_func(*args, **kwargs):
        print("this is do_func")
        func(*args, **kwargs)
        print("func run finished")
    print("this is the leave")
    return do_func


@wrapper
def run(name, age):
    print("{} : {}".format(name, age))


if __name__ == '__main__':
    # print("this is my first test python on xiaomi pc")
    run("zhansan", 12)