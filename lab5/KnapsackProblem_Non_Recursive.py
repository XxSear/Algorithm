# -*- coding:utf-8 -*-
import copy

#回溯法求解背包问题的非递归形式
#模拟递归求解时的堆栈情况，减去了递归求解时的出栈入栈过程


def Backtracking(goods,c):
    n = len(goods)
    res = []                         #用于存放最后结果
    pack = [0 for i in range(n)]    #背包的解向量
    weight = 0
    value = 0
    k  = 0                          #存放 当前对第几个物品操作, 用它来判断模拟的堆栈是否为空
    max = 0                         #存放 最优解
    count = 0                       #计算循环的次数
    while k >= 0:   #堆栈不为空
        while k < n :   #不停地往背包里加物品
            count += 1
            # print  "pack = ", pack, "value = ", value, "weight = ", weight, "k = ", k
            if weight + goods[k][1] <= c:
                pack[k] += 1
                value += goods[k][0]
                weight += goods[k][1]
            k += 1
        # print  "pack = ", pack, "value = ", value, "weight = ", weight, "k = ", k
        if value >= max:                    #记录背包内物品的最高价值
            max = value
            res.append( (copy.deepcopy( pack ),weight,value) )

        if k >= n: k -= 1                   #如果k大于n 将k置为n

        while pack[k] != 1 and k >= 0:     #找到存放的最后一个物品，将k指向其下标，k最低变为-1  之后就会推出循环
            k = k - 1

        if k >= 0:                          #将最后加入的一个物品取出来  接着遍历不加入goods[k]的情况
            pack[k] = 0
            value -= goods[k][0]
            weight -= goods[k][1]
            k += 1
    # print "count = ",count,"n = ",len(goods)
    return res,max













if __name__ == '__main__':
    # (价值,重量)
    goods = [ (1,2), (3,3), (5,4), (9,7), (4,2), (8,6), (10,12), (3,1), (1,1), (13,11), (2,2), (4,5), (5,7), (6,5), (7,7) ]
    # goods = [ (1,2), (3,3), (5,4), (9,7)]

    C = 12