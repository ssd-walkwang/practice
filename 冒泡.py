#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/27


def bubbleSort(alist):
    for j in range(len(alist) - 1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


li = [41, 22, 13, 84, 115, 6, 17, 58, 99, 210]
bubbleSort(li)
print(li)
