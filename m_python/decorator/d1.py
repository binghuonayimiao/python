import time
def f1():
    print('this is a function')
def f2():
    print('this is a function')
def decorator(fun):
    print(time.time())
    fun()
decorator(f1)
decorator(f2)