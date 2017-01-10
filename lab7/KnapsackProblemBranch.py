# -*- coding:utf-8 -*-
import Queue

#用队列（优先队列）形式实现分支限界法；
#采用贪心法作为界限函数的估计


#该类存储的是  在分支限界求解过程中，每一个节点的情况
class Item:
    # 构造的参数依次为  节点所在的层数  重量  价值  排序好的所有节点  已经选入背包的物品  将要选择的物品
    def __init__(self, level, w, v, node ,cap, select, isSelect ):
        self.level = level
        self.w = w
        self.v = v
        self.select = select
        if isSelect:
            self.select.append( node[1]  )
        self.MaxValue = v +  float( (cap - w) * node[0][0]) / node[0][1]    #分支限界法中使用的代价函数， F = 已经转入的物品价值 + 当前节点的重量价值比 * 背包剩余重量
    def __cmp__(self, other):               #重写该类的比较函数，使之能够使用优先队列进行选取
        if self.MaxValue < other.MaxValue:  #优先比较最大价值，当最大价值相同时，比较当前的重量，重量比较小的优先
            return -1
        elif self.MaxValue == other.MaxValue:
            if self.w < other.w:
                return 1
            elif self.w == other.w:
                return 0;
            else:
                return 01
        else:
            return 1
    def __str__(self):
        return "level = "+str( self.level)+" v = "+str(self.v)+" w = "+str(self.w)+" Mvalue = "+str(self.MaxValue)+" select = "+str(self.select)

#求解背包问题的类
class KBB:
    def __init__(self, cap, goods):
        self.capacity = cap
        self.goods = goods
        #对所有物品  按照重量价值比排序
        self.ordered = sorted( [((v,w),i) for i,(v,w) in enumerate(self.goods)],
                               key = lambda tup: float(tup[0][0])/tup[0][1], reverse = True )
        self.queue = Queue.PriorityQueue()  #用于存放节点的有限队列
        # for i in self.ordered:
        #     print i ,
        # print ""
        tmp = Item(-1, 0, 0, self.ordered[0], self.capacity, [], 0)
        self.queue.put(tmp)
        self.result = tmp

    def solution(self):
        if self.queue.qsize():  #只要优先队列不为空 就选出最优的节点 根据它计算两个派生的节点
            tmpItem = self.queue.get();
            # print tmpItem
            level = tmpItem.level + 1   #节点的层数+1
            if level < len(self.ordered) and tmpItem.w < self.capacity:     #是否如何最基本的限制条件
                node = self.ordered[level]                                   #将要加入的节点
                nextItem1 = Item( level, tmpItem.w, tmpItem.v, self.ordered[level], self.capacity , tmpItem.select, 0)      #不选择该节点的情况
                self.queue.put(nextItem1)
                if node[0][1] + tmpItem.w <=  self.capacity:                                                                #选择该节点的情况
                    nextItem2 = Item(level, tmpItem.w + node[0][1] , tmpItem.v + node[0][0], node, self.capacity, tmpItem.select, 1)
                    self.queue.put(nextItem2)
                self.solution()             #递归
            else:
                self.result = tmpItem   #不满足基本条件 说明该节点已经是最终结果
        return  self.result

if __name__ == '__main__':
    goods1 = [(1, 2), (3, 3), (5, 4), (9, 7), (4, 2), (8, 6), (10, 12), (3, 1), (1, 1), (13, 11), (2, 2), (4, 5),
              (5, 7), (6, 5), (7, 7)]
    goods = [(1, 2), (3, 3), (5, 4), (9, 7)]

    kp =  KBB(20, goods1)
    print kp.solution()

