# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort(key=lambda x: x == 0)
