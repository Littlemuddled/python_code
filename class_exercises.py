# 简单的多态实现
# class Dog(object):
#     def work(self):
#         print('狗正在工作')
#
#
# class PoliceDog(Dog):
#     pass
#
#
# class BindDog(Dog):
#     pass
#
#
# class DrugDog(Dog):
#     pass
#
#
# class Person(object):
#     __slots__ = ('dog', 'name') # 限制对象的属性只有 dog name
#     """
#     这是一个人类
#     """
#     def __init__(self, name):
#         self.dog = None
#         self.name = name
#
#     def work_with_dog(self):
#         self.dog.work()  # self就是创建的p对象 self.dog.work() == pd.work()  pd继承至Dog可以调用work方法  打印“狗正在工作”
#
#
# p = Person('张三')

# pd = PoliceDog()
# p.dog = pd
# p.work_with_dog()
#
# bd = BindDog()
# p.dog = bd
# p.work_with_dog()
#
# dd = DrugDog()
# p.dog = dd
# p.work_with_dog()

'''
 定义 get set 方法获取和设置私有变量
 普通方法  
 静态方法  @staticmethod  方法(函数)里面不使用任何的属性和对象  类名.静态方法名(参数，参数。。。)调用
 类方法    @classmethod   方法(函数)只用到了类属性，类名.类方法名() 或者 对象名.类方法名() 不需要手动传参  有cls
 
 单例设计模式：重写__new__方法，将多个对象的放在同一内存
 
 继承：深度优先  对象名.__mro__ 类属性可以查看方法的调用顺序
 
 is  isinstance 和 issubclass
 print(pi is p2)  is 身份运算符比较是否是同一个对象  实质是比较两个对象的内存地址 id(p1) == id(p2)
 isinstance(p,Person)  isinstance判断一个对象是否是由指定的类(或者父类)实例化出出来的
 issubclass(Student,Person)  issubclass判断一个类是否是另一个类的子类
 
 
'''

# print(dir(p))  # 列出所有对象的属性和方法（函数）
# print(p.__class__)  # <class '__main__.Person'>
# print(p.__dict__)  # {'dog': None, 'name': '张三'}  把对象属性和值转换成一个字典(但注意不能直接把一个对象当字典使用)
# print(p.__dir__())  # 等价于内置函数 dir(p)
# print(p.__doc__)  # 这是一个人类  看文档注释的
# print(Person.__doc__)  # 这是一个人类  看文档注释的  (两个都一样)
# print(p.__module__)  # __main__  打印模块名
import math

import self as self

'''
习题1
房子（House）有户型，总面积，剩余面积（总面积的%60），家具名称列表 属性
新房子没有任何的家具
将 家具的名称 追加到家具名称列表中
判断家具的面具是否超过剩余面积，如果超过提示不能添加此家具

家具（Furniture）有名字和占地面积属性，其中：
床垫（bed）   占地 4 平米
衣柜（chest） 占地 4 平米
餐桌（table） 占地 2 平米
将以上三件家具添加到房子中，
打印房子是要求输出：户型，总面积，剩余面积，家具名称列表
'''

# class House(object):
#     def __init__(self, house_type, total_area, free_list=None):
#         if free_list is None:  # 如果这个值是空的
#             free_list = []  # 将其值置为空列表
#         self.house_type = house_type
#         self.total_area = total_area
#         self.free_area = total_area * 0.6
#         self.free_list = free_list
#
#     def add_free(self, x):
#         if self.free_area < x.area:
#             print('剩余面积不足，放不进去了')
#         else:
#             self.free_list.append(x.name)
#             self.free_area -= x.area
#
#     def __str__(self):
#         return '户型={},总面积={},剩余面积={},家具列表={}.' \
#             .format(self.house_type, self.total_area, self.free_area, self.free_list)
#
#
# class Furniture(object):
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#
# # 创建房子对象
# house = House('两室一厅', 60, )
#
# # 创建家具对象
# sofa = Furniture('沙发', 30)
# bed = Furniture('床垫', 4)
# chest = Furniture('衣柜', 4)
# table = Furniture('餐桌', 2)
#
# # 把家具对象添加到房间里面
# # house.add_free(sofa)
# house.add_free(bed)
# house.add_free(chest)
# house.add_free(table)
#
# 打印房子 户型，总面积，剩余面积，家具名称列表
# print(house)
#
# 多态 封装 继承
# python 没有严格的多态  多态存在与继承中


'''
习题2             
设计两个类：
一个点（Point）属性包含 x，y 坐标
一个矩形类（Rectangle）属性有左上角和右上角的坐标
方法：1.计算矩形的面积 2.判断点是否在矩形内
实例 化一个对象，一个正方形对象，输入矩形的面积，输出点是否在矩形内
'''

# class Point(object):
#     def __init__(self, x: int, y: int):  # x y 为整型
#         self.x = x
#         self.y = y
#
#
# class Rectangle(object):
#     def __init__(self, top_left: Point, bottom_right: Point):  # top_left,bottom_right是Point类型的数据
#         self.top_left = top_left
#         self.bottom_right = bottom_right
#
#     def get_area(self):  # 得到面积
#         length = self.bottom_right.x - self.top_left.x
#         width = self.top_left.y - self.bottom_right.y
#         return length * width
#
#     def is_inside(self, point):  # 判断点是否在矩形内
#         return self.bottom_right.x > point.x > self.top_left.x and self.top_left.y > self.bottom_right.y
#
#
# p1 = Point(4, 20)  # 定义左上角的点
# p2 = Point(30, 8)  # 定义右下角的点
#
# r = Rectangle(p1, p2)  # 把左上角和右下角的点传给矩形
# print(r.get_area())  # (30-4)*(20-8) = 312
#
# p = Point(10, 13)
# print(r.is_inside(p))  # True
#
# x = Point(80, 20)
# print(r.is_inside(x))  # False


'''
定义一个点类 Pointer
属性是横向坐标 x 与纵向坐标 y
定义一个圆类 Circle
属性有圆心点（cp）和半径（radius）
方法有：
1.求圆的面积
2.求圆的周长
3.求指定点与圆的关系
关系有三种：【园内 园外 圆上】
涉及的数学公式：指定点与圆心点之间的距离 与 圆的半径进行比较
'''
#
# import math
#
#
# class Pointer(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Circle(object):
#     def __init__(self, cp, radius):
#         self.cp = cp
#         self.radius = radius
#
#     def get_area(self):
#         return str(self.radius ** 2 * math.pi) + '平方米'
#
#     def get_length(self):
#         return str(self.radius * 2 * math.pi) + '米'
#
#     def relationship(self, point):
#         """
#         判断一个点与圆心的关系：【园内 园外 圆上】
#         :param point: 需要判断的点
#         """
#         distance = (point.x - self.cp.x) ** 2 - (point.y - self.cp.y)
#         if distance > self.radius ** 2:
#             return '在圆外'
#         elif distance == self.radius ** 2:
#             return '在圆上'
#         else:
#             return '在园内'
#
#
# p = Pointer(0, 0)  # 创建了一个Pointer对象
# c = Circle(p, 3)  # 创建好的Pointer对象传递给了Circle的对象c
#
# print(c.get_area())
# print(c.get_length())
#
# p1 = Pointer(2, 3)
# print(c.relationship(p1))


'''
宠物店（PetShop）
属性：店名，店中的宠物【使用列表存储宠物】
方法：展示所有宠物的信息
宠物狗类（PetDog）
属性：昵称，性别，年龄，品种
方法：叫，拆家，吃饭
宠物猫类（PetCat）
属性：昵称，性别，年龄，品种，眼睛颜色
方法：叫，撒娇，吃饭
注意：狗的叫声是：汪汪    猫的叫声是:喵喵
     狗吃的是骨头       猫吃的是：鱼
'''
#
#
# class PetShop(object):
#     def __init__(self, store, pet_list=None):
#         self.store = store
#         if pet_list is None:
#             pet_list = []
#         self.pet_list = pet_list
#
#     def all_pet(self):
#         if len(self.pet_list) == 0:
#             print(f'{self.store}还没有宠物')
#             return
#         print(f'{self.store}有{len(self.pet_list)}个宠物，它们是：')
#         for pet in self.pet_list:
#             print(pet)
#
#
# class Pet(object):
#     def __init__(self, nickname, gender, age, breed):
#         self.nickname = nickname
#         self.gender = gender
#         self.age = age
#         self.breed = breed
#
#     def barking(self):
#         print(self.nickname + '正在叫')
#
#     def eat(self):
#         print(self.nickname + '正在吃')
#
#     def __str__(self):
#         return f'名字:{self.nickname},性别:{self.gender},年龄:{self.age},品种:{self.breed}'
#
#
# class PetDog(Pet):
#     def barking(self):
#         print(self.nickname + '正在汪汪汪')
#
#     def eat(self):
#         print(self.nickname + '正在吃骨头')
#
#     def demolition(self):
#         print(self.nickname + '正在拆家')
#
#
# class PetCat(Pet):
#     def __init__(self, nickname, gender, age, breed, eye_color):
#         super().__init__(nickname, gender, age, breed)
#         self.eye_color = eye_color
#
#     def barking(self):
#         print(self.nickname + '正在喵喵喵')
#
#     def eat(self):
#         print(self.nickname + '正在吃鱼')
#
#     def coquettish(self):
#         print(self.nickname + '正在撒娇')
#
#     def __str__(self):
#         return super().__str__() + f',眼睛颜色:{self.eye_color}'
#
#
# dog1 = PetDog('大黄', 'male', 2, '土狗')
# dog2 = PetDog('小黄', 'female', 1, '哈士奇')
# cat1 = PetCat('小白', 'female', 2.5, '加菲猫', '褐色')
# cat2 = PetCat('大黑', 'male', 2, '俄罗斯蓝猫', '蓝色')
#
# ps = PetShop('萌宠屋', [dog1, dog2, cat1, cat2])
# print(ps.all_pet())
#
# print(dog1)
# print(dog2)
# print(cat1)
# print(cat2)


'''
学生类 Student
    属性：学号，姓名，年龄，性别，成绩，
班级类 Grade
    属性：班级名称，班级中的学生【使用列表存储学生】
方法：
    1.查看该班级所有信息
    2.查看指定学号的学生信息
    3.查看班级中成绩不及格学生的信息
    4.将班级的学生成绩按照成绩降序排列
'''


class Student(object):
    def __init__(self, number, name, age, gender, score):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return f'学号:{self.number}, 姓名:{self.name}, 年龄:{self.age}, 性别:{self.gender}, 成绩:{self.score}'


class Grade(object):
    def __init__(self, grade_name, student_list=None):
        self.grade_name = grade_name
        if student_list is None:
            student_list = []
        self.student_list = student_list

    def show_all(self):
        for student in self.student_list:
            print(student)

    def show_one(self, number):
        for student in self.student_list:
            if student.number == number:
                print(student)

    def failed_student(self):
        # 方法1
        for student in self.student_list:
            if student.score < 60:
                print(student)
        # 方法2
        # result = filter(lambda student: student.score < 60, self.student_list)
        # for x in result:
        #     print(x)

    def order_score(self):
        # self.student_list.sort(key=lambda s: s.score)  # 直接改变原有列表
        return sorted(self.student_list, key=lambda s: s.score)  # 不会改变原有列表（创建一个新列表）


s1 = Student('001', '张三', 18, '男', 74)
s2 = Student('002', '李涵', 17, '女', 89)
s3 = Student('003', '王五', 18, '男', 56)
s4 = Student('004', '刘娟', 19, '女', 98)
s5 = Student('005', '唐浩', 18, '男', 68)
s6 = Student('006', '项羽', 19, '男', 48)

g = Grade('高三五班', [s1, s2, s3, s4, s5, s6])

# 直接修改
# g.order_score()  # 排序

g.show_all()
print()
g.show_one('002')
print()
g.failed_student()
print()

# 不修改创建一个新的
x = g.order_score()
for student in x:
    print(student)