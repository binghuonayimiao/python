# 闭包 = 函数+环境变量
def curve_pre():
    a = 10
    def curve(x):
        return  a*x*x
    return curve

f = curve_pre()
print(type(f))
print(f(2))
