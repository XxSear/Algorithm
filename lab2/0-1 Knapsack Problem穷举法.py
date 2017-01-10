# -*- coding:utf-8 -*-


#程序使用递归 遍历出所有解空间的集合，没有在递归中进行剪枝 所以程序的时间复杂度至少为O(m!)

# 在每次调用中程序调用函数，重复计算了背包中物品的价值和重量，所以程序的时间复杂度为O(n * n!)



goods = {}
C = 0
import copy
def stateOfpack(pack): #放回当前背包中的物品重量和价值和
    global goods
    global state_call
    state_call += 1
    weight = 0
    value = 0
    for i in pack:
        weight += goods[i][1]
        value += goods[i][0]
    return [weight,value]

#穷举法求解0-1背包问题
def loading(pack,res):

    global value, C, call, goods

    call += 1

    for i in goods:
        if i not in pack: #保证每种物品只能存放一次

            if goods[i][1] <= C - stateOfpack(pack)[0]: #如果背包有空余，则放入物品
                pack.append(i)

                tmp_state = stateOfpack(pack)
                if( tmp_state[1] > value):         # 如当前背包存放物品的价值大于最高纪录，则将其更新
                    res.append(copy.deepcopy(pack))
                    # print "res = ",res
                    value = tmp_state[1]

                loading(pack, res)          #在当前情况下递归调用自身
                pack.pop(-1)


if __name__ == '__main__':
    C = 10

    goods = {'v1': [1, 2], 'v2': [3, 3], 'v3': [5, 4], 'v4': [9, 7]}
    pack = []           #保存背包的存放状态
    res = []
    value = 0
    call = 0            #记录函数递归的次数
    state_call = 0         #记录调用state函数的次数

    loading(pack,res)
    print "res = ",res[-1]
    print "value = ",value,"  number_call",state_call,"  call = ",call


















