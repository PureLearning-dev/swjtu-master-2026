

class Person:
    # 这个 name 属于类是属性，存储在 __dict__ 中
    name = "Ajack"
    test = "测试 Person 类属性"
    # self 中的属性存储在每个示例中
    def __init__(self, name = "Tom", age = 18):
        print("Person Class Instance Init")
        self.name = name
        self.age = age

    def fun(self):
        print(self.test)

    def talk(self):
        print(self.name + "在说话")

    def move(self):
        print(self.name + "正在走路")

class Student(Person):
    def __init__(self, grade, name, age):
        print("Student Class Instance Init")
        super().__init__(name, age)
        self.grade = grade

    def move(self):
        print("年龄为" + str(self.age) + "的" + self.grade + "年级的" +self.name + "在上学的路上")

# Tom = Person("Tom", 20)
# Tom.move()
#
# Jack = Student("Middle", "Jack", 21)
# Jack.move()
# Jack.talk()
#
# print(Person.name)

print("Person.__dict__", Person.__dict__)

print("persion.__dict__", Person().__dict__)

# 先找对象实例是否存在 test 属性，不存在则查找类的 test 属性
Person().fun()