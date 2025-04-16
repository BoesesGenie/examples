# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        parentheses_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in parentheses_map:
                stack.append(char)

                continue

            if len(stack) == 0:
                return False

            check = stack.pop()

            if parentheses_map[check] != char:
                return False

        return len(stack) == 0

solution = Solution()

print(solution.isValid('()'))
print(solution.isValid('()[]{}'))
print(solution.isValid('(]'))
print(solution.isValid('([])'))
