# 函数的定义，函数体独立，其他代码包括注释要与函数相隔两行


def f():
    """这是函数注释"""
    print('HelloWorld')
f()

# 函数传参


def sum_2_num(num1, num2):
    """
    打印两数之和
    :param num1:
    :param num2:
    :return:
    """
    result = num1 + num2
    print('num1：%d和num2：%d的相加结果是：%d' % (num1, num2, result))
sum_2_num(1,2)