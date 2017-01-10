# -*- coding:utf-8 -*-
_author_ = 'PC'
import time

Fmin = 1000
Count = 0



#判断已经选择的路径 是否还能选择point
def findIsNextPoint(mat, path, point):
    if point not in path:
        if mat[path[-1]][point] > 0:
            if len(path) == len(mat) - 1:
                if mat[point][0] <= 0:
                    return False
            return True
    return False

#没有剪枝函数的回溯法

def findsol( mat, path, length, res):
    global Count
    Count += 1
    # print "path = ",path
    if len(path) == len(mat):   #如果路径长度等于节点长度，如果长度小于最优解 则记录该路径
        if len(res) == 0 or length < res[-1][1]:
            res.append( (path, length))
            print path, length

    if len(path) < len((mat)):
        for i in range(0, len(mat)):    #寻找合适的节点加入路径
            # print "path[-1] = ",path[-1], "i = ",i, "mat = ", mat[path[-1]] [i]
            if mat[path[-1]] [i] > 0:
                if findIsNextPoint(mat, path, i):
                    length += mat[path[-1]][i]
                    path.append(i)
                    findsol(mat, path, length, res)
                    path.pop(-1)
                    length -= mat[path[-1]][i]

#一个比较简单的剪枝函数
#传入参数为   矩阵，当前已经选择的路径，当前节点，当前已经选择的路径的长度
# 剪枝函数 F =  当前节点加入后路径的长度 +  未选择的节点各自最短路径之和
def functionOfCut(mat, path, i, length):
    global Fmin

    F = length + mat[path[-1]][i]
    for point in range(len(mat)):
        if point not in path and point != i:
            # print [k for k in mat[path[-1]] if k != 0]
            F += min( [k for k in mat[path[-1]] if k > 0] )
    return  F



def findsol_cut( mat, path, length):
    global Count
    Count += 1
    global Lmin
    global Fmin
    if len(path) == len(mat):   #记录最优解
        Fmin = length
        print path, length

    if len(path) < len(mat):
        for i in range(0, len(mat)):
            if mat[path[-1]][i] > 0:
                if findIsNextPoint(mat, path, i) and  functionOfCut(mat, path, i, length ) < Fmin: #将当前节点的情况代入剪枝函数 如果函数值大于当前最优值 则跳过
                    length += mat[path[-1]][i]
                    path.append(i)
                    findsol_cut(mat, path, length)
                    path.pop(-1)
                    length -= mat[path[-1]][i]


if __name__ == '__main__':

    data = [
        [0, 5, 9, 4 ],
        [5, 0, 0, 2 ],
        [9, 0, 0, 7 ],
        [4, 2, 7, 0 ]
    ]
    data1 = [[0, 4, 5, 9, -1, -1, 8, 1],
             [4, 0, 6, -1, 3, 3, 2, 4],
             [5, 6, 0, -1, -1, -1, 8, 5],
             [9, -1, -1, 0, 7, 4, 9, -1],
             [-1, 3, -1, 7, 0, 6, -1, 4],
             [-1, 3, -1, 4, 6, 0, -1, 3],
             [8, 2, 8, 9, -1, -1, 0, 1],
             [1, 4, 5, -1, 4, 3, 1, 0]]
    data2 = [
        [0, 4, 5, 9, -1, -1, 8, 3, 5, -1],
        [4, 0, 9, -1, 4, 7, 20, 4, -1, 23],
        [5, 9, 0, 22, 13, 2, -1, 11, 9, 2],
        [9, -1, 22, 0, 10, 4, 12, 5, 13, -1],
        [-1, 4, 13, 10, 0, -1, -1, 3, 23, 9],
        [-1, 7, 2, 4, -1, 0, 5, 2, -1, -1],
        [8, 20, -1, 13, -1, 5, 0, -1, -1, 12],
        [3, 4, 11, -1, 3, 2, -1, 0, 10, 9],
        [5, -1, 9, 13, 23, -1, -1, 10, 0, -1],
        [-1, 23, 2, -1, 9, -1, 12, 9, -1, 0],
    ]
    path = [0]
    length = 0
    res = []
    Count = 0
    time1 = time.time()
    findsol_cut( data2, path, length)
