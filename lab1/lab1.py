__author__ = 'user'

import mergesort
import quick_sort
import time
import random

if __name__ == '__main__':


    list = []
    for i in range(1000000):
        list.append( random.uniform(1,1000000))

    data = list
    # k = 0
    # for i in list:
    #     k += 1
    #     if k < 20:
    #         print i
    #
    # print "k = ",k
    # print "len(list)=",len(list)


    stime = time.time()
    print "quick_sort start = ",stime
    quick_sort.sort(data, 0, len(list)-1)
    otime = time.time()
    print "over_time = ",otime
    print "use time = ",otime - stime
    print "\n"

    data = list
    stime = time.time()
    print "mergesort start  = ",stime
    mergesort.mergesort(data)
    otime = time.time()
    print "over_time = ",otime
    print "use time = ",otime - stime

