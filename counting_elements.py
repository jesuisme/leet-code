"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

Constraints:
1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""


class Solution:
    def get_next(self, iterable):
        iterator = iter(iterable)
        try:
            current = next(iterator)
            for next_item in iterator:
                yield current, next_item
                current = next_item
        except StopIteration as e:
            return e

    def count_elements(self, arr: list) -> list:
        arr.sort()
        count = 0
        for current, next_item in self.get_next(arr):
            if current + 1 == next_item:
                appears = arr.count(current)
                count += appears

        return count


if __name__ == '__main__':
    sln = Solution()
    # print(sln.count_elements([1, 2, 3]))
    # print(sln.count_elements([1,3,2,3,5,0]))
    print(sln.count_elements([1,1,2,2]))
