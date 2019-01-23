# 判断空白字符

space_str1 = ""
space_str2 = " "
space_str3 = " a"
print(space_str1.isspace())  # Flase
print(space_str2.isspace())  # True
print(space_str3.isspace())  # False

# 判断字符串是否只包含数字
# 以下三个方法都不能判断小数

num_str1 = "1"
num_str2 = "\u00b2"
print(num_str2)
num_str3 = "一二三"

print(num_str1.isdecimal())  # True
print(num_str2.isdigit())  # True 除了判断以上一种类型字符，还可以判断unicode字符中的数字
print(num_str3.isnumeric())  # True 除了判断以上两种类型字符，还可以可以判断汉字数字