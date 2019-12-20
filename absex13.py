"""定义类Student,object是默认值"""
class Student(object):

# __init__是一个特殊方法，用于在创建对象时机型初始化操作
# 通过这个方法为学生对象绑定了name 和 age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.'%(self.name, course_name))

 __init__(self,"张晓明", 13)
 print(f"学生{self.name}，今年{self.age}岁！")
study(self,"高等化学")
