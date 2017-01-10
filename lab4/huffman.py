# -*- coding:utf-8 -*-
import Queue

#要求对任意给定的字符集与权重，输出最优前缀编码、平均码长


#传入构造好的  节点权重递减的链表
#返回根据 权重大小计算和对应位置 计算出的huffmanCode
def find_huffcode(list):

    huff_code = { list[0]: ''}    #包含所有字符的根节点
    # huff_code.update({list[0]:''})
    for postion in range(1,len(list)):
        pre = postion - 1
        while( list[postion] not in list[pre] ):    #找到当前位置以前的，包含目前字符的字符集位置
            pre -= 1

        if pre == postion - 1:                        #若当前字符集的前一个字符集的子集，说明当前字符是前一个字符集的左子树
            huff_code.update({ list[postion]: huff_code[list[pre]] + '0' } )
        else:                                          #若不是前一个字符集的子集，则往前依次寻找，直到找到符合条件的子集（最多会找到根节点）成为其右子树
            huff_code.update({list[postion]: huff_code[list[pre]] + '1'})
        # print "pos = ",postion, " pre = ",pre, "code = ",huff_code[list[postion]], list[postion]
    return huff_code

#该函数传入的是一个字典，将字典排序，时间复杂度较高，所以采用下面的函数，使用优先队列求解
# def creat_tree(dict):
#     tree = []
#     while len(dict) > 1:
#         list = sorted(dict.iteritems(), key=lambda d: d[1], reverse=False)
#         a = list[0]
#         b = list[1]
#         dict.pop(a[0])
#         dict.pop(b[0])
#         if len(a[0]) == 1:
#             tree.append(a[0])
#         if len(b[0]) == 1:
#             tree.append(b[0])
#         if a[1] > b[1]:
#             tmp = a[0] + b[0]
#         else:
#             tmp = b[0] + a[0]
#         total = a[1] + b[1]
#
#         tree.append(tmp)
#         dict.update({tmp: total})
#         print  tmp,":",total
#     return tree


#对给定的字符集及权重 求出Huffman Tree
#Huffman Tree 使用链表表示， 将每次取出的最小权重的字符依次放入链表
def creat_tree_v2(list):
    tree = []
    q = Queue.PriorityQueue()       #使用优先队列
    for i in list:
        q.put(i)
        # print i
    while q.qsize() > 1:
        min1 = q.get()              #每次取出两个最小的值
        min2 = q.get()

        if len(min2[1]) == 1:
            tree.append(min1[1])
            tree.append(min2[1])
        else:
            tree.append(min2[1])
            tree.append(min1[1])
        total = min1[0] + min2[0]
        code = min2[1] + min1[1]
        i = (total,code)
        q.put( i )                  #将两个值的权重相加，放入优先队列里

        # print total," ",min2[1]," ",min1[1]
    tree.append(q.get()[1])         #将优先队列中最后一个节点放入链表

    return tree


#计算huffmancode 和 原来编码的总长度
def test_huffcode(list, huffcode):
    length_pre = 0;
    length_now = 0;
    for i in list:
        length_pre += 8 * i[0]              #一个字符按8位计算
        length_now += len( huffcode[i[1]] ) * i[0]      #字符出现的次数 * 编码长度

    return length_pre, length_now




def huffman_code( list):
    # print "dict = ", dict
    # tree = creat_tree(dict)
    tree = creat_tree_v2(list)  #构造序列来表示huffmanTree
    tree = tree[::-1]           #将先前构造的反序列，从最大的开始计算huffmanCode
    print 'tree = ', tree

    huff_code = find_huffcode(tree)

    print "huff_code = ",huff_code

    length_pre, length_now = test_huffcode(list, huff_code)
    compress  = 1 - length_now/( 1.0 * length_pre)
    print "length_pre = ", length_pre,  " length_now = ", length_now, " compress  ",compress



if __name__ == '__main__':
    dict = {'a': 14, 'v': 28, 'c': 100, 'y': 1, 'e': 32, 'k': 12, 'p': 12, 'm': 34, 'w': 90}
    list = [(14, "a"), (28, "v"), (100, "c"), (1, "y"), (32, "e"), (12, "k"), (12, "p"), (34, "m"), (90, "w")]
    huffman_code(list)

























