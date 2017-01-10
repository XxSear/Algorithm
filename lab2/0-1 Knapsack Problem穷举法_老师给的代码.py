#!/usr/bin/env python
# coding=utf-8
__author__ = 'tonnytwo'

"""最简单的背包问题，背包最大容量是10  总共4件物品，价值和重量分别如下
Knapsack Max weight : W = 10 (units)
Total items         : N = 4
Values of items     : v[] = {10, 40, 30, 50}
Weight of items     : w[] = {5, 4, 6, 3}
"""

def goodIdea():
    V = [1, 3, 5, 9]
    W = [2, 3, 4, 7]
    MAX = 10
    print getValue(W,V,MAX,4)

#返回值 元组（最大总价值，背包剩余容量）
#输入
def getValue(W,V,MAX,i):

    #记录函数调用次数
    global count
    count = count + 1
    print count
    if(i>1):
        #不放第i件物品最大价值
        notV,notW = getValue(W,V,MAX,i-1)
        #放第i件物品的最大价值
        #如果第i件物品的重量大于背包最大容量
        if W[i-1]>MAX:
            return notV,notW
        else:#相反调整背包容量递归
            changeV,changeW = getValue(W,V,MAX - W[i-1],i-1)
            if changeV + V[i-1]>notV:
                    return changeV + V[i-1], changeW
            else:
                    return notV,notW
    else:
        if (W[0]>MAX):
            return 0,MAX
        else:
            return V[0],MAX-W[0]

count = 0
goodIdea()