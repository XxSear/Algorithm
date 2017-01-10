# -*- coding:utf-8 -*-
import copy

#回溯法求解背包问题




max = 0
count = 0

def loading(goods, res, pack, weight, value, pos, c):
    global  count
    global max
    count += 1
    if weight <= c:                          #若背包重量大于C 则结束此次调用
        if value >= max:                     #如果重量小于C 且 当前背包价值大于等于 max  则记录当前背包的情况
            max = value
            res.append( (copy.deepcopy(pack),weight,value))

        for i in  range(pos, len(goods)):   #从传入的下标依次选取背包
            pack.append(i)                                                                 #更新背包的情况 递归调用自己
            loading(goods, res, pack, weight+goods[i][1], value + goods[i][0], i+1, c)
            pack.pop(-1)

#该函数 接收loading函数返回的值，从中选出最大价值的选择方式，并以链表的形式返回
def select_res(res):
    global max
    final_res = []
    for i in range(len(res))[::-1]:
        if  res[i][2] < max:
            break;
        final_res.append( res[i])
    return final_res

def solve(goods, C):
    weight = 0
    value = 0
    pos = 0
    pack = []
    res = []
    loading(goods,res, pack, weight, value, pos, C)
    final_res = select_res(res)
    print final_res

if __name__ == '__main__':
    # (价值,重量)
    goods = [ (1,2), (3,3), (5,4), (9,7), (4,2), (8,6), (10,9), (3,1), (4,1), (13,11), (2,2), (4,3), (5,7), (6,5), (8,7) ]
    C = 18
    solve(goods,C)