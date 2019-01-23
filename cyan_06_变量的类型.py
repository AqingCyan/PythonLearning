"""
python中定义变量是不需要指定类型的
数据类型可以分为数字型和非数字型
数字型：整型、浮点型、布尔型、复数型
非数字型：字符串、列表、元组、字典

type可以知道数据类型
"""

a = 9.0
name = 'Cyan'
print(type(a))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(2 ** 64))
# 在参与算数计算的时候，True会转换为1， False会转换为0
i = 10
b1 = True
b2 = False
print(10 * b1)  # 10
print(10 * b2)  # 0

# 字符串的拼接
first_name = 'Cyan'
last_name = 'Aqing'
my_name = first_name + last_name
print(my_name)
print('-' * 10)  # 输出10个‘-’
# print(i + 'Cyan') py没有数字到字符串的自动转换
