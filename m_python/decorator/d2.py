import time
def decorator(fun):
    def wrapper():
        print(time.time())
        fun()
    return wrapper
def f1():
    print('this is a function')
f = decorator(f1)
f()