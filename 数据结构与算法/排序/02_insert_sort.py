# coding: utf-8


def insert_sort(alist):
    """插入排序"""
    i = 1
    if alist[i] < alist[i-1]:
        alist[i], alist[i-1] = alist[i-1], alist[i]
