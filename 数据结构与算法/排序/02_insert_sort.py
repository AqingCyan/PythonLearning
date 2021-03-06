# coding: utf-8


def insert_sort(nums):
    """插入排序"""
    for j in range(1, len(nums)):
        # j代表，从右边的无序列中取出多少个元素执行这样的过程
        i = j
        # i代表内层循环起始值
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
            else:
                break
    return nums


list = insert_sort([3, 1, 4, 2, 5, 2, 1])
print(list)