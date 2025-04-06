# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        divider = 10
        current = num % divider
        result = ''
        symbols_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        while num > 0:
            if current in symbols_map:
                result = symbols_map[current] + result
            elif current > 0:
                base = divider / 10
                multiplier = int(current / base)
                five_base = ''

                if multiplier > 5:
                    five_base = symbols_map[base * 5]
                    multiplier -= 5

                result = five_base + multiplier * symbols_map[base] + result

            num -= current
            divider *= 10
            current = num % divider

        return result
