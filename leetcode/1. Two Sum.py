#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/8/5 10:54

base Info
"""
__author__ = 'xx'
__version__ = '1.0'

#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for idx in range(length):
            diff = target - nums[idx]
            try:
                pos = nums[idx+1:].index(diff)          #两个数字可能相同  但位置不同

                return [idx, idx + 1 + pos]
            except:
                pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))






