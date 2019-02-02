# coding: utf-8
# 时间复杂度是：O(n)


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0  # 用count记录交换次数
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:  # 如果count等于0，未发生交换，说明列表有序，直接break
            break
    return alist


l = bubble_sort([3,1,4,2,5,2,1])
print(l)