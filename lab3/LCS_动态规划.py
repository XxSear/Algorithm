# -*- coding:utf-8 -*-

#使用动态规划求解LCS问题
#用i,j分别表示两个序列的下标 C[i,j]表示Xi,Yj的最长公共子序列的长度
#优化函数：   当i,j>0 and xi = yi  时  C[i,j] =   C[i-1][j-1]+1  此时标记函数用*表示
#             当i,j>0 and x1 != y1 时  C[i,j] = max{ C[i,j-1], C[i-1,j]}  此时标记函数用 < 和 ^ 表示
#             当 i = 0 or j = 0 时   C[i,j] = 0

# 算法的时间复杂度为 O(n^2)


#传入参数为两个序列
#函数返回两个表 优化函数 和 标记函数
def LCS_AP(A, B):
    res = []    #标记函数
    tag = []    #优化函数
    line1 = [0 for i in range(0,len(A)+1)]    #将优化函数表的第一行初始化为0
    res.append(line1)
    for i in range(1 , len(A) + 1):
        line = []           #用于暂时存储该行的 优化函数值 和 标记函数值
        tag_tmp = []
        line.append(0)      #j = 0 时 优化函数为0
        for j in range(1,len(B) + 1):
            # print "i = ",i," j = ",j
            if B[i-1] == A[j-1]:        #第一种情况 *
                line.append(res[i-1][j-1] + 1)
                tag_tmp.append('*')
                # print "=",i,j
            else:
                if res[i-1][j] >= line[j-1]:    #   ^
                    line.append(res[i-1][j])
                    tag_tmp.append('^')
                else:                           #   <
                    line.append(line[j-1])
                    tag_tmp.append('<')
        print line
        print tag_tmp
        tag.append(tag_tmp)
        res.append(line)
    return res,tag

#从标记函数中 找到一个公共序列
def LCS_AP_find_equence(A, B, x, y, tag, res):
    # print "x = ",x," y = ",y," ",tag[y][x]
    if x < 0 or y < 0:          #根据标记函数，依次寻找对应位置的符号，将表中所有的*标记的函数串联起来，就最长的公共子序列
        # print "res = ",res
        return res
    else:
        if tag[y][x] == '^':
            LCS_AP_find_equence(A, B, x, y-1, tag, res)
        if tag[y][x] == '<':
            LCS_AP_find_equence(A, B, x-1, y, tag, res)
        if tag[y][x] == '*':
            res.append(x)
            LCS_AP_find_equence(A, B, x-1, y-1, tag, res)


def LCS_Dynamic_programming(A,B):
    print "使用动态规划求解"
    record, tag =  LCS_AP(A ,B)
    ways = []
    LCS_AP_find_equence(A, B, len(A)-1, len(B)-1, tag, ways)
    ways.reverse()              #因为是从后往前找，所以需要将链表中的结果反转
    print "way = ", ways
    print "结果为 ",
    for i in ways:
        print A[i],


if __name__ == '__main__':

    A = ["a","b","c","d","e"]
    B = ["b","d","e","a","f"]
    LCS_Dynamic_programming(A, B)
