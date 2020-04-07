"""
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/
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

    def maxProfit(self, prices: list) -> int:
        profit = 0
        for current, next_item in self.get_next(prices):
            if next_item > current:
                profit = profit + (next_item - current)
        return profit


if __name__ == '__main__':
    sln = Solution()
    print(sln.maxProfit([7,1,5,3,6,4]))
