# coding:utf-8
def binary_search(li, item):
    """二分查找"""
    n = len(li)
    if n > 0:
        mid = n // 2
        if li[mid] == item:
            return True
        elif item < li[mid]:
            return binary_search(li[:mid], item)
        else:
            return binary_search(li[mid + 1:], item)
    else:
        return False

# 测试用例
list = [10, 12, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94]
print(binary_search(list, 59))
print(binary_search(list, 100))
