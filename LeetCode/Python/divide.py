# https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    def divide_unsigned(self, dividend, divisor):
        result = 0
        rem = dividend

        while rem >= divisor:
            rem -= divisor
            result += 1

        return result

    def divide(self, dividend, divisor):
        if dividend < 0:
            return -self.divide(-dividend, divisor)
        if divisor < 0:
            return -self.divide(dividend, -divisor)

        return self.divide_unsigned(dividend, divisor)
