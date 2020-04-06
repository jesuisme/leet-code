# Write an algorithm to determine if a number n is "happy".
# https://leetcode.com/problems/happy-number/

class Solution:
    def compute_happy(self, num: int) -> int:
        num_string = str(num)
        happy_sum = 0
        for digit in num_string:
            happy_sum = happy_sum + (int(digit)**2)
        return happy_sum
        
    def isHappy(self, n: int) -> bool:
        happy_list = []
        happy_number = self.compute_happy(n)
        while happy_number not in happy_list:
            if happy_number == 1:
                return True
            else:
                happy_list.append(happy_number)
                happy_number = self.compute_happy(happy_number)
        return False
