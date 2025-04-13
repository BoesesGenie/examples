# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    digits_letter_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(self.digits_letter_map[digits[0]])

        last = digits[-1]
        result = []

        for next_letters in self.letterCombinations(digits[:-1]):
            for letter in self.letterCombinations(last):
                result.append(next_letters + letter)

        return result

solution = Solution()

print(solution.letterCombinations('23'))
print(solution.letterCombinations(''))
print(solution.letterCombinations('2'))
print(solution.letterCombinations('234'))
