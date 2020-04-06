# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# https://leetcode.com/problems/maximum-subarray/
#
# I couldn't quite figure out how to do the recursion so I looked up another solution to the problem
# My non-recursive solution used too much memory

# Non-recursive attempt
class NotSolution:
    def get_slices(self, number_list: list, slice_length: int) -> list:
        if slice_length >= len(number_list) or slice_length <= 0:
            return [number_list]

        stop_index = len(number_list) - slice_length
        slice_list = []

        for i in range(stop_index + 1):
            slice = number_list[i:slice_length + i]
            slice_list.append(slice)

        return slice_list

    def maxSubArray(self, nums: list) -> int:
        subarray_list = []
        for i in range(1, len(nums) + 1):
            subarray_list = subarray_list + self.get_slices(nums, i)

        subarray_sums = [sum(subarray) for subarray in subarray_list]
        return max(subarray_sums)

class Solution:
    def add_slices(self, subarray):
        length_of_slice = len(subarray)
        
        # fundamental case
        if length_of_slice == 1:
            return subarray[0], subarray[0], subarray[0], subarray[0]  # Same value for all sums
        
        midpoint = length_of_slice // 2
        a = subarray[:midpoint]  # left
        b = subarray[midpoint:]  # right

        # recursion for sub-subarrays
        a_sum, a_left, a_right, a_best = self.add_slices(a)
        b_sum, b_left, b_right, b_best = self.add_slices(b)

        # merging results O(1)
        recursive_sum = a_sum + b_sum
        recursive_left = max(a_sum + max(0, b_left), a_left)
        recursive_right = max(b_sum + max(0, a_right), b_right)
        recursive_best = max(recursive_sum, recursive_left, recursive_right, a_right + b_left, a_best, b_best)

        # return tuple
        return recursive_sum, recursive_left, recursive_right, recursive_best
        
    def maxSubArray(self, nums: List[int]) -> int:
        return self.add_slices(nums)[-1]
