# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        current = digits[i] + 1
        digits[i] = current if current < 10 else 0
        rem = 0 if current < 10 else 1

        if not rem:
            return digits

        i -= 1

        while i >= 0:
            current = digits[i] + rem

            rem = 0 if current < 10 else 1

            digits[i] = current if current < 10 else 0

            if not rem:
                break

            i -= 1

        if rem:
            digits.insert(0, 1)

        return digits