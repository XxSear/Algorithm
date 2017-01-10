# -*- coding:utf-8 -*-

# 统计归并算法中数据的比较和交换的次数
number_compare = 0
number_swap = 0

def mergesort(seq):
	if len(seq) <= 1: #能再分割
		return seq

	mid=int(len(seq)/2)   #将链表从中间分割
	left=mergesort(seq[:mid])
	right=mergesort(seq[mid:])

	return merge(left,right) #完全分割后 调用合并函数

def merge(left,right):
	result=[]
	i,j=0,0
	# 将左两个链表中的数据归并到一个链表
	while i<len(left) and j<len(right):
		# number_compare += 1
		if left[i]<=right[j]:
			result.append(left[i])
            # number_swap += 1
			i+=1
		else:
			result.append(right[j])
			j+=1
	# 因为链表是从一个一个的数字合并而来，所以链表内部是有序的
	# 虽然下面将左右两个剩余的链表都加到res的末尾，但经过上面的循环，left[i:]与right[j:]中有一个为空
	result+=left[i:]
	result+=right[j:]
	# 经过以上处理，将两个链表合并，且链表内部是有序的
	return result

if __name__=='__main__':
	seq=[4,5,7,9,7,5,1,0,7,2,3,99,6,13]
	print(mergesort(seq))



