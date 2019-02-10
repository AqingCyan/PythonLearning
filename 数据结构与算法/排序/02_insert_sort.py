# coding: utf-8


def insert_sort(alist):
    """插入排序"""
    for j in range(1, len(alist)):
        # j代表，从右边的无序列中取出多少个元素执行这样的过程
        i = j
        # i代表内层循环起始值
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist 


l = insert_sort([3,1,4,2,5,2,1])
print(l)