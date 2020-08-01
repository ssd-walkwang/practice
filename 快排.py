#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/27


def quickSort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quickSort(alist, start, low-1)
    quickSort(alist, low+1, end)


li = [24, 55, 60, 11, 2, 44, 36, 27]
quickSort(li, 0, len(li)-1)
print(li)