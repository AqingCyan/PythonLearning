# 使打印文本有格式
poem = ['静夜思', '李白', '床前白月光', '疑是地上霜', '举头望明月', '低头思故乡']

for poem_str in poem:
    print("|%s|" % poem_str.center(10))  # 因为填充的是英文空格，所以居中不尽如人意


for poem_str in poem:
    print("|%s|" % poem_str.center(10, "1"))  # 我们可以指定填充的内容

for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "1"))  # 我们可以指定填充的内容