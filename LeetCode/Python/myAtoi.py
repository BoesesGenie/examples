class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()

        if not s:
            return 0

        digits_start = False
        value_start = False
        result = []
        mult = 1
        counter = 0
        index = 0
        MAX = ['2', '1', '4', '7', '4', '8', '3', '6', '4', '7']
        MAX_DIGITS = 10
        outOfRange = True

        if s[0] == '-':
            mult = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for char in s:
            if char == '0' and not digits_start:
                digits_start = True

                continue

            if char == '0' and not value_start:
                continue

            if not char.isdigit() and not digits_start:
                return 0

            if not char.isdigit() and not value_start:
                return 0

            if not char.isdigit() and value_start:
                break

            if char.isdigit() and not digits_start:
                digits_start = True

            if char.isdigit() and not value_start:
                value_start = True

            counter = counter + 1

            if counter > MAX_DIGITS and mult == -1:
                return -2147483648

            if counter > MAX_DIGITS and mult == 1:
                return 2147483647

            result.append(char)

            if counter == MAX_DIGITS:
                for num in MAX:
                    if outOfRange and result[index] < num:
                        outOfRange = False

                    if result[index] > num and mult == -1 and outOfRange:
                        return -2147483648
                    if result[index] > num and mult == 1 and outOfRange:
                        return 2147483647

                    index = index + 1

        if len(result) == 0:
            return 0

        return int(''.join(result)) * mult
