# 有参数和关键字参数的情况
import time
def decorator(fun):
    def wrapper(*args, **kw): # 既可以支持多参数也可以支持关键字参数
        print(time.time())
        fun(*args, **kw)
    return wrapper
@decorator # 装饰器的精髓
def f1(name): 
    print('this is a function of ' + name)
f1('f1')

@decorator # 装饰器的精髓
def f2(name1, name2): 
    print('this is a function of ' + name1 + name2)
f2('f2', 'f22')

@decorator # 装饰器的精髓
def f3(name1, name2, **kw): 
    print('this is a function of ' + name1 + name2)
    print(kw)
f3('f2', 'f22', a = 1, b = 2, c =3 )