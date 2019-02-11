def quick_sort(nums, first, last):
    """快速排序"""
    if first >= last:  # 递归终止条件
        return
    mid_value = nums[first]  # 把第一个数作为中间元素
    low = first  # low游标从开头游动
    height = last  # height游标从尾巴游动
    while low < height:
        # 先让height游标左移
        while low < height and nums[height] >= mid_value:  # 把相等值的情况放到一边处理即可，保证mid_value是分割线
            height -= 1
        nums[low] = nums[height]
        # 再让low游标右移
        while low < height and nums[low] < mid_value:
            low += 1
        nums[height] = nums[low]
    # 从整个循环退出时，low是等于height的
    nums[low] = mid_value
    # 对low左边的列表执行快排，对low右边的列表快排
    quick_sort(nums, first, low - 1)
    quick_sort(nums, low + 1, last)


nums = [12, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
