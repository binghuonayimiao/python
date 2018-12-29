from fatherClass import Human
class Student(Human):
    school = "lele"
    def __init__(self, school, name, age):
        self.school = school
        # 记住第一个参数是self,因为是拿类名调用的，如果是实例调用的就不需要了
        # Human.__init__(self, name, age)
        # 第二种调用父类方法最多
        super(Student, self).__init__(name, age)

student = Student('光明小学', '啦啦', 19)
# print(student.sum)
# print(student.name)
# print(student.age)
# 下面这种调用可行，但是几乎没这么做的 
Student.my_print(student)