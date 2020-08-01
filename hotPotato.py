#! /usr/bin/env python
# *-* coding:utf8 *-*
# author: DSS time:2020/7/25


from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue((simqueue.dequeue()))

        simqueue.dequeue()

        return simqueue.dequeue()


print(hotPotato(["A", "B", "C", "D", "E", "F", "G"], 7))
