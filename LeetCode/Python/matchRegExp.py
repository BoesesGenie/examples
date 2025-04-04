# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def match_reg_exp(self, s, p):
        m = len(s)
        n = len(p)
        M = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        M[0][0] = True

        i = 1
        while i < n + 1:
            if p[i - 1] == '*':
                M[0][i] = M[0][i - 2]

            i += 1

        i = 1

        while i < m + 1:
            j = 1
            while j < n + 1:
                current_s = s[i - 1]
                current_p = p[j - 1]

                if current_s == current_p or current_p == '.':
                    M[i][j] = M[i - 1][j - 1]

                elif current_p == '*':
                    prev = p[j - 2]
                    if prev != '.' and prev != current_s:
                        M[i][j] = M[i][j - 2]
                    else:
                        M[i][j] = M[i - 1][j] or M[i][j - 1] or M[i][j - 2]

                j += 1

            i += 1

        return M[m][n]
