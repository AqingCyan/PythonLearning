def merge_sort(nums):
    """归并排序"""
    n = len(nums)
    if n <= 1:  # 递归退出条件，不再拆分了
        return nums
    mid = n // 2
    # left 采用归并排序后形成的有序的新的列表
    left_list = merge_sort(nums[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_list = merge_sort(nums[mid:])
    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0  # 两个指针
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):  # 两个指针的其中一个在移动的时候如果越界了说明排序完成
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 如果左指针越界退出循环，右边的列表还有末尾一个未取完，把它拿进来，右边同理，下面的处理是对描述情况的处理，所以其中一行必然取的是空列表
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result

# 测试用例
list = [12, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
print(merge_sort(list))