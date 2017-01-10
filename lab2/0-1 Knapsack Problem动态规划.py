# -*- coding:utf-8 -*-
import copy

# 使用动态规划求解0-1背包问题
# 设背包承受重量为y 物品的种类数为k
#  优化函数  Fk(y) = max{ Fk-1(y), Fk(y - wk) + vk }

# 根据上式可以将背包问题的所有情况遍历出来

number_compare = 0
def bag(n, c, w, v):
    global number_compare
    res = [[-1 for j in range(c+1)] for i in range(n+1)]   #构造 (c +1 ) * （n + 1） 的矩阵 用于存储遍历时产生的所有情况
    tag = copy.deepcopy(res)                                             #构造  (c +1 ) * （n + 1） 的 标记函数 存储优化函数的每次选择情况
    # print 'res = ', res

    for j in range(c+1):
        res[0][j] = 0   #矩阵第一行为 物品总数为0的情况，所有取值均为0
    for i in range(n+1):
        res[i][0] = 0  #矩阵第一列为  背包承受重量为0的情况 取值均为0

    for k in range(1, n+1):
        for y in range(1, c+1):

            tag[k][y] = tag[k - 1][y]
            # 一下语句实现优化函数的功能
            res[k][y] = res[k-1][y]

            if y - w[k-1] >= 0 and res[k-1][y] < res[k][y - w[k-1]] + v[k - 1]:
                if tag[k][y - w[k - 1]] != k:  # 保证每种物品只能存放一次
                    res[k][y] = res[k][y - w[k-1]] + v[k - 1]
                else:
                    res[k][y] = res[k][y - w[k - 1]]
                tag[k][y] = k   #标记函数存储 背包中放置的最后一件物品的下标

    return res,tag



def show_res(n, c, w, res, tag):
    print'最大价值为:', res[n][c]
    #goods为背包中物品的下标  通过k y 在标记函数中通过结果向前追踪
    goods = []
    k = n
    y = c

    while tag[k][y] != -1:
        print k, y
        line =  tag[k][y]
        if line == k:           #最优情况下 物品在这一行被放置，所以将此物品存入结果
            goods.append(tag[k][y])
            y -= w[k-1]
        else:
            k = line

    print "背包放置的物品为",goods

if __name__ == '__main__':
    n = 4
    c = 10
    w = [2, 3, 4, 7]
    v = [1, 3, 5, 9]
    print 'w = ',w
    print 'v = ',v
    res,tag = bag(n, c, w, v)
    # for i in res:
    #     print i
    # for i in tag:
    #     print i
    show_res(n, c, w, res, tag)


# 使用动态规划求解0-1背包问题
# 程序中需要遍历一个 n*c 大小的矩阵 其时间复杂度为 O(n*c) , 而在第二个函数 追踪求解的时间复杂度为O(n)

# 所以该算法总体的时间复杂度为O(n*c)
