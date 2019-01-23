# 如果a+b+c=1000，且a^2+b^2=c^2（abc皆为自然数），求出a、b、c可能的组合？

# a
# b
# c
# 方法2：如果知道a与b，c就是1000-a-b
import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0,1001):
        c = 1000 - a - b # 去掉了C的循环遍历，直接计算它
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" %(a, b, c))
end_time = time.time()
print("times:%.02fs，now finished" %(end_time - start_time))
