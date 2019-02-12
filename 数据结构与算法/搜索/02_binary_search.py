def binary_search(li, item):
    """二分查找非递归"""
    n = len(li)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if li[mid] == item:
            return mid
        elif item < li[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

# 测试用例
list = [10, 12, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94]
print(binary_search(list, 59))
print(binary_search(list, 100))