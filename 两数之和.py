#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/28


def twoSum(nums, target):

    n = len(nums)
    for i in range(1, n):
        j = -1
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j >= 0:
        return[j, i]
x = [2,7,11,15]
y = 9
twoSum(x,y)
