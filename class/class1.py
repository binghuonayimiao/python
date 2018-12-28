class Student():
    name = 'zgs' #实例变量
    age = 18  #实例变量
    sum = 0   #类变量
    def __init__(self, name, age):
        #Student.sum += 1
        self.__class__.sum += 1
        self.name = name
        self.age = age
        print(name, age)

    def print_student(self):
        print("name = " + self.name)
        print('age = ' + str(self.age))

    @classmethod  #类方法，可以直接调用类变量
    def plus_sum(cls):
        cls.sum += 1
        print(cls.age)
        print(cls.sum)

    @staticmethod
    #不需要self，也可以用类名和实例变量访问
    def add(x, y):
        return x + y


student = Student('lll', 1111)
student.plus_sum()#最好不要用实例去掉用类方法，逻辑上说不通
#也可以用类名调用
Student.plus_sum()
student1 = Student('aa', 555)
student1.plus_sum()
#print('sum = ' + str(Student.sum))