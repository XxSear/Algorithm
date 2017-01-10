# -*- coding:utf-8 -*-
_author_ = 'PC'
import math
import itertools

number_full = 0   #计算
number_divede = 0

a = [1,2,3,4,5,6,7,8,9,10]
a = [1,2,3]
# 穷举法
# a为需要排序的元素构成的list  n为从第几位开始交换
def arrange(a,n):
    global number_full
    if n == len(a):
        print a,number_full
    else:
        for i in range(n-1, len(a)):
            a[n - 1],a[i] = a[i],a[n - 1]
            number_full += 1
            arrange(a, n+1)
            a[n - 1], a[i] = a[i], a[n - 1]


# 分治法
# res为存储结果的list
def divede_arrange(a, n, res):
    global number_divede
    if len(res) == len(a):
        # print res
        res
    else:
        for i in range(0,len(res)+1):
            # print "i = ",i,"len = ",len(res)
            res.insert(i,a[n-1])
            number_divede += 1
            divede_arrange(a, n+1, res)
            res.pop(i)


arrange(a,1)
print " n = ",len(a),"时，运算 ", number_full,"次 n! = ",math.factorial(len(a))
# res = []
# divede_arrange(a, 1, res)
# print " n = ",len(a),"时，运算 ", number_divede,"次 n! = ",math.factorial(len(a))

# print res



# res = []
# a = [1]
# for i in range(2,11):
#     a.append(i)
#     number_divede = 0
#     divede_arrange(a, 1, res)
#     print " n = ", len(a), "时，运算 ", number_divede, "次,  n! = ", math.factorial(len(a))
    # number_full = 0
    # arrange(a,1)

    # print " n = ",len(a),"时，运算 ", number_full,"次 n! = ",math.factorial(len(a))
