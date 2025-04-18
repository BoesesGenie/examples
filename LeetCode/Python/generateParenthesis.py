# https://leetcode.com/problems/generate-parentheses/
# NB: the algorithm can be optimized!

from itertools import product

class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)

                continue

            if len(stack) == 0:
                return False

            stack.pop()

            if char != ')':
                return False

        return len(stack) == 0

    def generateParenthesis(self, n):
        return list(filter(self.isValid, [''.join(x) for x in product(['(', ')'], repeat = n * 2)]))

solution = Solution()

print(solution.generateParenthesis(3))
