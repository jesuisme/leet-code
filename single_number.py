# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: list) -> int:
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) == 1:
                return num
