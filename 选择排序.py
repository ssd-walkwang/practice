'''
@Author: your name
@Date: 2020-07-27 23:34:05
@LastEditTime: 2020-07-29 22:40:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \新建文件夹\选择排序.py
'''
#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/27


def selectionSort(alist):
    n = len(alist)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if alist[j] < alist[minIndex]:
                minIndex = j
        if minIndex != 1:
            alist[i], alist[minIndex] = alist[minIndex], alist[i]


li=[12, 45, 77, 95, 12, 25, 64, 24]
selectionSort(li)
print(li)