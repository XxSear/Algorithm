#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/8/5 19:46

base Info
"""
__author__ = 'xx'
__version__ = '1.0'
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

 

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        return self.divi_array(nums1, nums2)


    def divi_array(self, num1, num2):
        print(num1, num2)
        if len(num2) <= 3 or len(num1) <= 3  :
            num1.extend(num2)
            num1.sort()
            mid_pos = len(num1) // 2
            if len(num1) % 2 == 0:
                return (num1[mid_pos - 1] + num1[mid_pos]) / 2
            else:
                return num1[mid_pos]


        if num1[0] > num2[0]:  # 保证num1[0] <= num2[0]
            tmp = num1
            num1 = num2
            num2 = tmp

        if num1[-1] <= num2[0]:  #分离
            num1.extend(num2)
            mid_pos = len(num1) // 2
            # print(num1)
            if len(num1) % 2 == 0:
                return (num1[mid_pos - 1] + num1[mid_pos])/2
            else:
                return num1[mid_pos]

        # if num1[-1] >= num2[-1]:  #包括
        mid_pos_1 = len(num1) // 2
        mid_pos_2 = len(num2) // 2
        mid_pos = min(mid_pos_1,mid_pos_2)
        # print( num1[-mid_pos] , num2[-mid_pos])
        if num1[-mid_pos] <= num2[-mid_pos]:
            num2 = num2[:-mid_pos]
        else:
            num1 = num1[:-mid_pos]

        if num1[mid_pos-1] >= num2[mid_pos-1]:
            num2 = num2[mid_pos:]
        else:
            num1 = num1[mid_pos:]
        return self.divi_array(num1, num2)

        # else: # 有交集
        #
        #     mid_pos_1 = len(num1) // 2
        #     mid_pos_2 = len(num2) // 2
        #     mid_pos = min(mid_pos_1,mid_pos_2)
        #
        #     num1 = num1[mid_pos:]
        #     if num1[-mid_pos] <= num2[-mid_pos]:
        #         num2 = num2[:mid_pos]
        #
        #     return self.divi_array( num1, num2 )   #正确？








if __name__ == '__main__':
    # num1 = [1,2,4,5,7,18,19,20]
    num1 = [1,2,6,7]
    num2 = [3,4,5,8]
    # num2 = [6,8,12,16,22,36]
    sol = Solution()
    print(sol.findMedianSortedArrays(num1, num2))













