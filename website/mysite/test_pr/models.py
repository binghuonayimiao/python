# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
 


class StudentManager(models.Manager):
    def add(self, a, b):
        return a+b
    def create_student(self, name):
        # 方式一
        # student = Student(name = name)
        # # 保存到数据库
        # student.save()
        # 方式二(推荐)
        student = self.create(name)
        return student
 
    def select_all(self):
        # 查询全部
        list = self.all()
        return list
 
    def select_one(self, name):
        # a = []
        # # 查询单条数据
        # student = self.get(id=id)
        # a.append(student)
        # return a
        # 查询匹配条件的多条数据
        # student = self.filter(name=name)
        # 模糊查询
        student = self.filter(name__contains=name)
        # 根据字段内容排序后展示数据，根据字段内容逆向排序后展示数据,加一个负号order_by('-name')
        tt = student.order_by('name')
 
        # 限制数据条数, 相当于mysql limit
        tt1 = self.filter(name__contains=name)[0:5]  # [0]显示第一条 [0:2]会显示前两条，切片不支持负数
        return tt1
 
    def updata_student(self, id, name):
        self.get(id=id).update(name=name)  # update可多条update(name=name, bb="wahaha")
 
# Create your models here.
class Student(models.Model):
 
    # 如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=20)
 
    # model的字符串表现形式1
    def __unicode__(self):
        return self.name
 
    objects = StudentManager()
 
 
