# -*- coding:utf-8 -*-
Fmin = 1000000
Count = 0


#判断已经选择的路径 是否还能选择point
def findIsNextPoint(mat, path, point):
    # print "test path = ",path," point = ",point
    if point not in path:
        if point not in path  and  mat[path[-1]][point] > 0:
            if len(path) == len(mat) - 1:
                if mat[point][0] <= 0:
                    return False

            return True
    return False

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

def findsolNotRecursive(mat):
    global Count
    Count += 1
    global Fmin
    path = [0]
    length = 0
    pos = 1
    flag = False
    while len(path) > 0:
        while pos < len(mat):       #不停往链表里加东西，直到不能加为止

            # print path, pos, len(path)
            if findIsNextPoint(mat, path, pos) and functionOfCut(mat, path, pos, length) < Fmin:   #若成功加入，pos重置为1
                length += mat[path[-1]][pos]
                # print "j = ",path[-1],"x = ",pos," value = ",mat[path[-1]][pos]," length = ",length
                path.append(pos)
                pos = 1
            else:       #若结点未加入成功 pos+1
                pos += 1
            if len(path) == len(mat):  #若所有节点均加入路径，得到一种结果
                Fmin = length
                print "path = ",path," Fmin = ",Fmin
                flag = True
                break


        tmp = path.pop(-1)  #取出路径中的最后一个
        # print "tmp = ", tmp
        if tmp == 0:        #若为0 说明 解空间已经被搜索或是裁剪完毕，可以推出循环
            break
        else:
            length -= mat[path[-1]][tmp]    #否则搜索下一个节点
            pos = tmp+1



if __name__ == '__main__':
    data = [[0, 4, 5, 9, -1, -1, 8, 1],
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

    findsolNotRecursive(data2)