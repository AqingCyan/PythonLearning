# 如果a+b+c=1000，且a^2+b^2=c^2（abc皆为自然数），求出a、b、c可能的组合？

# a
# b
# c
# 方法1：暴力枚举法，把所有的数字遍历，求出来
import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" %(a, b, c))
end_time = time.time()
print("times:%ds，now finished" %(end_time - start_time))
