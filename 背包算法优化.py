#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/26


def MaxVal2(memo, w, v, index, last):
    """
    得到最大价值
    w为widght
    v为value
    index为索引
    last为剩余重量
    """

    global numCount
    numCount = numCount + 1

    try:
        # 以往是否计算过分支，如果计算过，直接返回分支的结果
        return memo[(index, last)]
    except:
        # 最底部
        if index == 0:
            # 是否可以装入
            if w[index] <= last:
                return v[index]
            else:
                return 0

                # 寻找可以装入的分支
        without_l = MaxVal2(memo, w, v, index - 1, last)

        # 如果当前的分支大于约束
        # 返回历史查找的最大值
        if w[index] > last:
            return without_l
        else:
            # 当前分支加入背包，剪掉背包剩余重量，继续寻找
            with_l = v[index] + MaxVal2(memo, w, v, index - 1, last - w[index])

            # 比较最大值
        maxvalue = max(with_l, without_l)
        # 存储
        memo[(index, last)] = maxvalue
        return maxvalue


w = [0, 1, 4, 3, 1]  # 东西的重量
v = [0, 1500, 3000, 2000, 2000]  # 东西的价值

numCount = 0
memo = {}
n = len(w) - 1
m = 4
print(MaxVal2(memo, w, v, n, m), "caculate count : ", numCount)

# 4000 caculate count :  20