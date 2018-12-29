import time
def decorator(fun):
    def wrapper():
        print(time.time())
        fun()
    return wrapper
@decorator # 装饰器的精髓
def f1():
    print('this is a function')
f1()