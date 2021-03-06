# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 使用双指针遍历法：
    # 其中index用于记录去重后所得新数组最后一个元素的位置
    # index指针追寻i指针，i指针用来遍历
    # 当遇到i和index所指向的元素值不同时，把i所指元素的值拷贝到新数组最后一个位置（index所在位置），然后将index向后移动一位。
    # 当遇到i和index所指的元素值相同时，不对index进行处理，只移动i
    if len(nums) == 1 or len(nums) == 0: return len(nums)
    index = 1
    i = 1
    while i < len(nums):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
        i += 1
    return index


# 测试用例
# 输入：[-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-26,-25,-25,-24,-24,-24,-22,-22,-21,-21,-21,-21,-21,-20,-19,-18,-18,-18,-17,-17,-17,-17,-17,-16,-16,-15,-14,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,10,11,11,12,12,13,13,13,14,14,14,15,16,17,17,18,20,21,22,22,22,23,23,25,26,28,29,29,29,30,31,31,32,33,34,34,34,36,36,37,37,38,38,38,39,40,40,40,41,42,42,43,43,44,44,45,45,45,46,47,47,47,47,48,49,49,49,50]
# 预期：[-50,-49,-48,-47,-46,-45,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-28,-27,-26,-25,-24,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-10,-9,-8,-7,-6,-5,-4,-3,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,25,26,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

nums = [-50, -50, -49, -48, -47, -47, -47, -46, -45, -43, -42, -41, -40, -40, -40, -40, -40, -40, -39, -38, -38, -38,
        -38,
        -37, -36, -35, -34, -34, -34, -33, -32, -31, -30, -28, -27, -26, -26, -26, -25, -25, -24, -24, -24, -22, -22,
        -21,
        -21, -21, -21, -21, -20, -19, -18, -18, -18, -17, -17, -17, -17, -17, -16, -16, -15, -14, -14, -14, -13, -13,
        -12,
        -12, -10, -10, -9, -8, -8, -7, -7, -6, -5, -4, -4, -4, -3, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10,
        10,
        11, 11, 12, 12, 13, 13, 13, 14, 14, 14, 15, 16, 17, 17, 18, 20, 21, 22, 22, 22, 23, 23, 25, 26, 28, 29, 29, 29,
        30,
        31, 31, 32, 33, 34, 34, 34, 36, 36, 37, 37, 38, 38, 38, 39, 40, 40, 40, 41, 42, 42, 43, 43, 44, 44, 45, 45, 45,
        46,
        47, 47, 47, 47, 48, 49, 49, 49, 50]
print(len(nums))
len = removeDuplicates(nums)
print(len)
print(nums)
