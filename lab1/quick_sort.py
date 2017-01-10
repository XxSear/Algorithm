# -*- coding:utf-8 -*-

# 快排的基本思想：每一次划分 选取end位的数据为标志，把比它小的数放到左边，比它大的数放到右边
# 每一次划分将数列中的一个数据排好位置，然后再分别排列左右两边的数据

number_compare = 0
number_swap = 0

def partition(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        raise ValueError("list which lenght is less then 2 do not need to partition")

    key = li[end]    #key为选出的标签，函数将根据其=它划分数据
    middle_index = start

    # 遍历数据，若小于key则将其换到左边
    for x in xrange(start, end):
        if li[x] < key:
            li[middle_index], li[x] = li[x], li[middle_index]
            middle_index += 1
    li[end], li[middle_index] = li[middle_index], li[end] #将key换到中间的位置
    return middle_index


def sort(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        return li

    middle_index = partition(li, start, end)   #middle_index为这一次划分排列好的数据，根据其将链表划分为两端，分别递归调用sort排序
    sort(li, start, middle_index - 1)
    sort(li, middle_index + 1, end)
    return li


def main():
    l = [2, 3, 4, 23, 45, 6, 9, 12, 134, 4, 6, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = sort(l, 0, len(l) - 1)
    print li


if __name__ == '__main__':
    main()


