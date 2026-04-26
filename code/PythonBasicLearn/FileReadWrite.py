# 向文件中写入内容

file_text = "你好呀！\n我是一个文件内容。"

# 默认是在当前文件夹中创建文件
file_path = "test.txt"
file_path2 = "/Users/purelearning/Desktop/test.txt"
file_stream = open(file_path, "w")
file_stream2 = open(file_path2, "w")

print("# 开始写入内容到文件中")

file_stream.write(file_text)
file_stream2.write(file_text)

print("# 创建文件并写入成功")

file_stream.close()
file_stream2.close()

print("# 文件流关闭成功")

# 读取文件中的内容

read_file = open(file_path, "r")

print("# 开始读取文件中的内容")

# 使用 read 得到的内容使用之后直接就没了，后面无法再次对 read_file 执行其他读取方法！
# 此后的 流 对象也是同样的

# 一次性读取到文件中的所有内容
once_read_content = read_file.read()

print("# 一次性读取到的内容", once_read_content)

read_file.close()

read_file2 = open(file_path, "r")

# 返回一个 list，文件中的每一行内容存在一个索引中
all_lines = read_file2.readlines()

print("# readlines得到的内容", all_lines)

print("# 使用 for 循环便利readlines中的内容")

for line in all_lines:
    print(line)

read_file2.close()

# 使用迭代器对文件内容进行读取，等价使用 readline
read_file3 = open(file_path, "r")

print("# 一行一行的读取文件中的内容")

for line in read_file3:
    print(line)

read_file3.close()

print("# 使用 readline 读取文件内容")

read_file4 = open(file_path, "r")

while True:
    line = read_file4.readline()
    if not line:
        break
    print(line)

read_file4.close()

# 对于上述的一个 流 对象只能调用一种读取方法，其本质是 指针 ！
# 在读取时，会创建一个指针指向文件的开始，每次读取后，就会移动指针，读取完，指针就指向末尾，故不能继续使用了
# 可以重新打开得到新的 流 对象，或者使用 seek 函数移动指针