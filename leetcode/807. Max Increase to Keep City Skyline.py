#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/8/5 10:05

base Info
"""
__author__ = 'xx'
__version__ = '1.0'
# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.
#
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
#
# What is the maximum total sum that the height of the buildings can be increased?
#
# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
#
# The grid after increasing the height of buildings without affecting skylines is:
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid[0])
        # grid = np.array(grid)
        # rows_max = grid.max(axis=0)   # 每一行的最大值
        rows_max = [max(row) for row in grid]

        # lines_max = grid.max(axis=1)  # 每一列的最大值
        lines_max = []
        increased_height = 0
        for idx in range(length):
            line_max = max( [ grid[row][idx] for row in range(length)] )
            lines_max.append(line_max)

        # new_mat = np.zeros((length, length))
        # print(rows_max)
        # print(lines_max)
        # new_mat = []
        for row_idx in range(length):
            # new_row = []
            for line_idx in range(length):
                # new_row.append( min( rows_max[row_idx], lines_max[line_idx] ))
                increased_height +=  min( rows_max[row_idx], lines_max[line_idx] ) - grid[row_idx][line_idx]
            # new_mat.append(new_row)
        # return new_mat
        return increased_height

if __name__ == '__main__':
    grid = [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0] ]

    # sol = Solution()
    # print(sol.maxIncreaseKeepingSkyline(grid))
    print([max(col) for col in zip(*grid)])   # 二维数组转置！
