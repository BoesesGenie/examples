class Solution(object):
    def romanToInt(self, s):
        prev = 0
        result = 0
        i = len(s) - 1
        symbols_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        while i >= 0:
            if symbols_map[s[i]] < prev:
                result -= symbols_map[s[i]]
            else:
                result += symbols_map[s[i]]

            prev = symbols_map[s[i]]
            i -= 1

        return result
