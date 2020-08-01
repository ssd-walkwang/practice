#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/27


def insertSort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


li = [14, 15, 75, 99, 56, 37, 81, 2, 100]
insertSort(li)
print(li)
