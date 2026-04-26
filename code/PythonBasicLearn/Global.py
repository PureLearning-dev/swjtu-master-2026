Global = 100
a = None

# 在函数内部可以使用 global 关键字进行全局变量的修改，若不使用 global，在函数内部重新创建一个局部变量 a，则会导致无法修改全局变量a
# 也就是当在局部中需要修改全局变量的值时，需要使用 global 关键字
def fun():
    global a
    a = 20
    return a + 100

def fun2():
    a = 20
    return a + 10

print("a pass was", a)
print("local variable a is", fun2())
print("a now is", fun())
