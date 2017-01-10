# -*- coding:utf-8 -*-
_author_ = 'PC'

import KnapsackProblem  as KP
import time
count = 0


def OneTest(goods, c):
    res = []
    max = 0

    print "C = ", c, " number of goods = ", len(goods)
    time1 = time.time()
    res, max = KP.Backtracking(goods, c)
    final_res = KP.select_res(res)
    time2 = time.time()
    print "非递归耗时 = ", time2 - time1

    weight = 0
    value = 0
    pos = 0
    pack = []
    res = []
    count = 0

    time3 = time.time()
    KP.loading(goods, res, pack, weight, value, pos, c)
    final_res = KP.select_res(res)
    time4 = time.time()
    print "递归耗时 = ", time4 - time3


if __name__ == '__main__':
    # (价值,重量)
    goods1 = [ (1,2), (3,3), (5,4), (9,7), (4,2), (8,6), (10,12), (3,1), (1,1), (13,11), (2,2), (4,5), (5,7), (6,5), (7,7) ]
    goods2 = [ (1,2), (3,3), (5,4), (9,7),(10,12), (3,1), (1,1), (13,11), (2,2), (4,5), (5,7), (6,5), (7,7), (13,14), (23,21), (2,1), (1,4), (5,4)]
    goods3 = [(1, 2), (3, 3), (5, 4), (9, 7), (10, 12), (3, 1), (1, 1), (13, 11), (2, 2), (4, 5), (5, 7), (6, 5),
              (7, 7), (13, 14), (23, 21), (2, 1), (1, 4), (5, 4)]
    goods4 = [(1, 2), (3, 3), (5, 4), (9, 7), (10, 12), (3, 1), (1, 1), (13, 11), (2, 2), (4, 5), (5, 7), (6, 5),
              (7, 7), (13, 14), (23, 21), (2, 1), (1, 4), (5, 4), (13, 14), (23, 21), (2, 1), (1, 4), (5, 4), (30, 29),
              (14, 15)]
    goods5 = [(1, 2), (3, 3), (5, 4), (9, 7), (10, 12), (3, 1), (1, 1), (13, 11), (2, 2), (4, 5), (5, 7), (6, 5),
              (7, 7), (13, 14), (23, 21), (2, 1), (1, 4), (5, 4), (13, 14), (23, 21), (2, 1), (1, 4), (5, 4),(30,29),(14,15)]

    testOfgoods = []
    testOfgoods.append( (goods1, 30))
    testOfgoods.append( (goods2, 40))
    testOfgoods.append( (goods3, 50))
    testOfgoods.append((goods4, 70))
    testOfgoods.append( (goods5, 80))

    for i in testOfgoods:
        OneTest(i[0], i[1])
        print
