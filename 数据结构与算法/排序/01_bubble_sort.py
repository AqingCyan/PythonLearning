# coding: utf-8
# 时间复杂度是：O(n)


def bubble_sort(nums):
    """冒泡排序"""
    n = len(nums)
    for j in range(n-1):
        count = 0  # 用count记录交换次数
        for i in range(0, n-1-j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
        if 0 == count:  # 如果count等于0，未发生交换，说明列表有序，直接break
            break
    return nums


list = bubble_sort([3, 1, 4, 2, 5, 2, 1])
print(list)