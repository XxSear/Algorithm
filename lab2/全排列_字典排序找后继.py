# -*- coding:utf-8 -*-
_author_ = 'PC'



def next( a ):

    # 找到峰值
    for i in reversed( range(len(a)) ):
        if a[i] > a[i - 1]:
            top = i
            break
    # print "top = ",top
    # 找到交换的数----峰值右边 大于a[top-1] 中最小的数
    mm = top
    for i in range(top + 1, len(a)):
        if a[i] > a[top-1]:
            mm = i ;

    # /颠倒后面的数
    a[top - 1], a[mm] = a[mm] , a[top - 1]
    i = 0
    x = (top+len(a))/2 - top
    while i <= x :
        a[i+top], a[len(a) - i -1] = a[len(a) - i -1], a[i+top]
        i += 1



def hasNext(a):
    for i in reversed( range(1,len(a)) ):
        if a[i] > a[i - 1]:
            return 1
    return 0;


if __name__ == '__main__':

    a = [1, 4, 2, 5, 3]
    while(hasNext(a)):
        next(a)
        print a
