import re

# 正则匹配的作用是为了在一堆字符中找到自己需要的内容，格式很多很杂，在需要时进行查询使用即可

simple_expression = "abc"

total_text = "cfeacbcdef"

# 判断是否在一个字符串中存在，最简单的使用方法
print(simple_expression in total_text)

re_expression = "bcd"

re_pattern = r"c[df]e"

# 正则查找，若存在会返回找到的详细信息，否则返回 None
# 可以使用 [a-z0-9] 等格式进行简化
print(re.search(re_expression, total_text))

# 使用正则表达式，在字符串前面添加一个 r 则可，只会返回查找的第一个情况，后续的就算满足条件也不会返回了
print(re.search(re_pattern, total_text))
