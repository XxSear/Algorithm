#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/8/5 11:03

base Info
"""
__author__ = 'xx'
__version__ = '1.0'

'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


https://leetcode.com/problems/4sum/discuss/128591/Easy-to-understand-python-Solution
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = self.k_Sum(nums, target, 0, 0, 4)
        uni_res = []
        for item in res:
            if item not in uni_res:
                uni_res.append(item)
        return uni_res

    def k_Sum(self, nums, target, sum, start, k):   # O( N^k )
        result = []
        # print(nums, target, start, k)
        for idx in range(start, len(nums)):
            tmp_sum = sum + nums[idx]
            if tmp_sum <= target or nums[idx] < 0:                              # 超时  裁剪
                if k == 1:
                    if tmp_sum == target:
                        result.append([nums[idx]])
                else:
                    tmp_res = self.k_Sum(nums, target, tmp_sum, idx+1, k - 1)
                    # print(tmp_res)
                    for i in tmp_res:
                        tmp_list = [nums[idx]]
                        tmp_list.extend(i)
                        result.append(tmp_list)

        return result


    def hash_4_sum(self, nums, target):
        nums.sort()
        one_hash = {}
        for idx in range(len(nums)):
            key = nums[idx]
            value = idx
            if  key in one_hash:
                one_hash[key].append(value)
            else:
                one_hash[key] = [value]

        # print(one_hash)
        two_sum_hash = {}  # sum:[factor]
        one_hash_key = list( one_hash.keys() )
        # print(one_hash_key)
        # print(type(one_hash_key))
        len_key = len(one_hash_key)
        for rank1 in range(len_key):
            for rank2 in range(rank1, len_key):

                key = one_hash_key[rank1] + one_hash_key[rank2]
                value = ( one_hash_key[rank1] ,one_hash_key[rank2])
                if key in two_sum_hash:
                    two_sum_hash[key].append(value)
                    # two_sum_hash[key] = value
                else:
                    two_sum_hash[key] = [value]

        # search factor
        res = []
        for one_key in two_sum_hash.keys():
            diff = target - one_key
            if diff in two_sum_hash:    #找到四个数
                x1_x2 = two_sum_hash[one_key]            #[(x1,x2),()]
                x3_x4 = two_sum_hash[diff]

                for factor1,factor2 in x1_x2:
                    for factor3, factor4 in x3_x4:
                        # print([factor1, factor2, factor3, factor4])
                        idx_list = [one_hash[factor1],one_hash[factor2],one_hash[factor3],one_hash[factor4],]
                        if self.varif_res(idx_list, len(nums)):
                            # print([factor1,factor2,factor3,factor4])
                            one_res = [factor1,factor2,factor3,factor4]
                            one_res.sort()
                            if one_res not in res:
                                res.append(one_res)
                        # res.append([factor1,factor2,factor3,factor4])
                        # print([factor1,factor2,factor3,factor4])
        # res = list(set(res))
        res.sort()


        return res

        # print( res )
    def varif_res(self, factors, n):
        verifi_list = [1 for i in range(n)]
        for factor in factors:
            try:
                tag = False
                for idx in factor:
                    if  verifi_list[idx]:
                        verifi_list[idx] = 0
                        tag = True
                        break
                if tag:
                    continue
                else:
                    return False
            except:
                return False

        return True

if __name__ == '__main__':
    sol = Solution()
    # nums = [-499,-483,-463,-461,-431,-417,-390,-381,-366,-365,-342,-339,-321,-290,-285,-272,-265,-258,-228,-211,-188,-182,-146,-144,-123,-120,-112,-97,-92,-60,-58,-53,-53,-41,-36,-28,-15,-12,-7,22,45,57,59,62,77,81,99,103,105,115,119,135,147,154,169,183,187,215,243,258,259,266,272,272,275,309,319,345,370,382,385,389,436,439,442,469,484]
    # target = 7189
    # print(sol.fourSum(nums, 7189))
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.hash_4_sum(nums, target))