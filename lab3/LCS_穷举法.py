# -*- coding:utf-8 -*-
_author_ = 'PC'
import copy
import math

#使用穷举法求解TSP问题
#首先遍历出A的所有子序列，把他们一个个带入序列B 计算出其公共序列的长度
# 算法遍历出所有A的序列 需要O(2^n)的时间复杂度
# 而对每个序列求解 又需要O(n)的时间复杂度
# 所以 改程序的时间复杂度为O(n*2^n)

# 遍历出所有的序列  用 01表示
def LCS_full_sequence(select, position, res):
    res.append( copy.deepcopy(select))
    for i in range(position,len(select)):
        select[i] = 1
        LCS_full_sequence(select,position+1,res)
        select[i] = 0

# 传入一个A,B序列和一种选择方法
# 寻找公共子列的长度,返回其长度
def IsPublicSequence(A,B,select):
    tag = 0
    same = 0
    sequence = []
    for i in range(len(A)):
        if select[i]:
            sequence.append(A[i])
    # print "sequence is ",sequence
    for i in sequence:
        while(tag < len(B)):
            if i == B[tag]:
                same += 1
                tag += 1
                break;
            tag += 1
    return same


#暴力求解的函数接口,传入A B两个序列,返回最长的公共子序列
def LCS_Brute_force(A,B):
    print "使用穷举法求解"
    select = [0 for i in range(len(A))]
    res = []                            #用于存放2^n中 序列A的选择情况
    final_squence = []
    LCS_full_sequence(select, 0, res)


    max = 0
    PubilicSquence = []
    for i in res:                       #将res中 A的左右可能序列 去与 B序列比较，看其公共的序列长度,并记录下最长序列的情况
        # print "test ", i
        if max < IsPublicSequence(A, B, i):
            PubilicSquence = i
            max = IsPublicSequence(A, B, i)

    for i in range(len(A)):
        if PubilicSquence[i]:
            final_squence.append(A[i])
    print "最长的公共子序列长度为 = ", max
    print "结果为 ",
    print final_squence
    return final_squence


if __name__ == '__main__':
    A = ["a", "b", "c", "d", "e"]
    B = ["b", "d", "e", "a", "f"]
    LCS_Brute_force(A,B)
