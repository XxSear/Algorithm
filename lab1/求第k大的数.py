# -*- coding:utf-8 -*-
__author__ = 'user'
import random

# 给定线性序集中n个元素和一个整数k，1≤k≤n，要求找出这n个元素中第k小的元素

def search(list, k):
    if k > len(list) or k < 0:
        print "out of range"
        return -1

    pointVal = list[ random.randint( 0, len(list) - 1 ) ]
    # 随机生成一个下标 找到其对应的值 将其作为标记为 给序列中的数据分类
    print "k = ",k, " pointVal = ",pointVal,
    left = []
    right = []
    for i in list:
        if pointVal >= i:
            left.append(i)
        else:
            right.append(i)

    print  "  length of left = ",len(left),"   length of right = ",len(right)

    # 程序中 将与pointVal值相同的数据分到了左边，如果左边的长度与我们所求的k值相等，则pointVal就是我们所求的答案
    if len(left) == k:
        print "find the k-th largest number", pointVal
        return pointVal

    # 如果没找到结果，就递归地寻找left和right子串
    else:
        if len(left) > k :
           return  search(left,k)
        else:
           return  search(right,k - len(left)) #递归寻找右边的子串时需要将k值减去左子串的长度


# 算法的复杂度分析
# T(n) = T(n/2) + cn
# 根据主定理第三条 T(n) = O(n)

if __name__ == '__main__':
    list = []
    for i in range(1000000):
        list.append(random.uniform(1, 1000000))

    test = [1, 5, 8, 9, 3]

    search(list, 1000)
