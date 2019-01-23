# 我们采用不同的方法来创建1到10000的list，并且使用timeit来测算运行1000次所用时间
from timeit import Timer

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li += [i]

def t3():
    li = [i for i in range(10000)]

def t4():
    li = list(range(10000))

# timeit模块参数都是字符串，Timer的 第一个参数是要测试的函数
# timer1.timeit可以指定运行多少次，返回值是运行时间，单位是s

timer1 = Timer("t1()", "from __main__ import t1")
print("append:", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("+:", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("[for i in rang(10000)]:", timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("list(range(10000)):", timer4.timeit(1000))