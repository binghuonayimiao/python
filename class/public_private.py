class Student():
    name = 'zgs' # 实例变量
    age = 18  # 实例变量
    __score = 0  #私有变量
    sum = 0   # 类变量
    def __init__(self, name, age):
        # Student.sum += 1
        self.__class__.sum += 1
        self.name = name
        self.age = age
        # print(name, age)

    def marking(self, score):
        if score < 0:
            print("score is not unnormal")
            return
        self.__score = score
        print(self.name + " score is " + str(self.__score))

student1 = Student("zs", 12)
# 下面两行不报错，不是代表可以访问私有变量，而是因为.代表新添加了一个变量
student1.__socre = -1
print(student1.__socre)