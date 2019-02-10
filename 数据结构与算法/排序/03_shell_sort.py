def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2  # 分组的步长
    # gap变化到0之前，插入算法执行的次数
    while gap >= 1:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            # i的起始永远从gap起始
            i = j
            # 排序的次数
            while i > 0:  # 通过一个循环，通用所有列的排序，建议画图理解
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短步长，列分的更细了
        gap //= 2
    return alist

# 测试用例
nums = [12, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
print(shell_sort(nums))