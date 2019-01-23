hello_str = "hello world"

# 1.判断字符串是否以指定字符串开始
print(hello_str.startswith('hello'))  # True，区分大小写

# 2.判断字符串是否以指定字符串结束
print(hello_str.endswith('world'))  # True，区分大小写

# 3.查找指定字符串
print(hello_str.find('o '))  # 4，在第五个位置出现
print(hello_str.find('a'))  # -1，不存在

# 4.替换字符串
print(hello_str.replace('world', 'python'))  # hello python
print(hello_str)  # hello world，说明replace方法不修改原字符串