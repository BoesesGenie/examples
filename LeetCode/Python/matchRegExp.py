class Solution:
    completed = False
    status = False
    s_left = 0
    s_right = 0
    p_index = 0
    s = ''
    p = ''
    prev = (0, 0, 0)

    def initial_values(self):
        self.completed = False
        self.status = False
        self.s_left = 0
        self.s_right = 0
        self.p_index = 0
        self.s = ''
        self.p = ''
        self.prev = (0, 0, 0)

    def update_state(self):
        if self.s_right == len(self.s) and self.p_index == len(self.p):
            self.completed = True
            self.status = True

        elif self.s_left == len(self.s) and self.p_index == len(self.p):
            self.completed = True
            self.status = True

        elif self.p_index == len(self.p) and self.s_right < len(self.s):
            self.completed = True
            self.status = False

        elif self.p_index == len(self.p) and self.s_left > len(self.s):
            # print(self.s_left, self.s_right, self.p_index)
            self.completed = True
            self.status = False

    def handle_mult(self):
        check = self.p[self.p_index - 1]

        self.s_left -= 1
        self.s_right -=1

        while self.s_right < len(self.s):
            if check == '.' or check == self.s[self.s_right]:
                self.s_right += 1
            else:
                break

        # print(self.s_left, self.s_right, self.p_index)

        self.p_index += 1

    def handle_dot(self):
        if self.s_left >= len(self.s):
            self.s_left += 1
            self.s_right = max(self.s_right, self.s_left)
        elif self.s_left == self.s_right:
            self.s_left += 1
            self.s_right += 1
        else:
            while self.s_left < self.s_right:
                self.s_left += 1

            self.s_left += 1
            self.s_right = max(self.s_right, self.s_left)

        self.p_index += 1

    def handle_letter(self):
        if self.s_left >= len(self.s):
            self.s_left += 1
            self.s_right = max(self.s_right, self.s_left)
        elif self.s_left == self.s_right and self.p[self.p_index] == self.s[self.s_left]:
            self.s_left += 1
            self.s_right += 1
        elif self.s_left != self.s_right:
            while self.s_left < self.s_right and self.p[self.p_index] != self.s[self.s_left]:
                self.s_left += 1

            self.s_left += 1
            self.s_right = max(self.s_right, self.s_left)

        self.p_index += 1

    def match_reg_exp(self, s, p):
        self.initial_values()
        self.s = s
        self.p = p

        while not self.completed:
            if p[self.p_index] == '*':
                self.handle_mult()
                self.update_state()
                continue

            if p[self.p_index] == '.':
                self.handle_dot()
                self.update_state()
                continue

            self.handle_letter()
            self.update_state()

        return self.status

solution = Solution()

# print(solution.match_reg_exp('abc', 'abc') == True)
# print(solution.match_reg_exp('abc', '.*') == True)
# print(solution.match_reg_exp('abc', '...') == True)
# print(solution.match_reg_exp('abc', '..') == False)
# print(solution.match_reg_exp('abc', '....') == False)
# print(solution.match_reg_exp('abc', 'abd') == False)
# print(solution.match_reg_exp('abc', 'cbc') == False)
# print(solution.match_reg_exp('abc', '.bc') == True)
# print(solution.match_reg_exp('abc', 'a.c') == True)
# print(solution.match_reg_exp('abc', 'ab.') == True)
# print(solution.match_reg_exp('abc', '..c') == True)
# print(solution.match_reg_exp('abc', '.*c') == True)
# print(solution.match_reg_exp('asdfasdfabc', '.*abc') == True)
# print(solution.match_reg_exp('asdfasdfabc', '........abc') == True)
# print(solution.match_reg_exp('asdfasdfabc', '.......abc') == False)
# print(solution.match_reg_exp('asdfamdfabc', 'asd.*abc') == True)
# print(solution.match_reg_exp('asdfasdfabc', 'asd.*abc') == True)
# print(solution.match_reg_exp('asdfasdfabc', 'asd.*') == True)
# print(solution.match_reg_exp('asm', '.*asd') == False)
# print(solution.match_reg_exp('aa', 'a') == False)
# print(solution.match_reg_exp('mississippi', 'mis*is*ip*.') == True)
# print(solution.match_reg_exp('abcd', 'd*') == False)
# print(solution.match_reg_exp('aaa', 'aaaa') == False)
# print(solution.match_reg_exp('a', 'ab*a') == False)
# print(solution.match_reg_exp('asd', 'asd.*') == True)
# print(solution.match_reg_exp('abb', 'bbb*') == False)
# print(solution.match_reg_exp('asd', '.*asd') == True)
# print(solution.match_reg_exp('aa', 'a*') == True)
# print(solution.match_reg_exp('aa', '.*..a*') == False)
print(solution.match_reg_exp('aaa', 'ab*a*c*a') == True)
# print(solution.match_reg_exp('aab', 'c*a*b') == True)
# print(solution.match_reg_exp('a', 'c*a') == True)
# print(solution.match_reg_exp('aba', '.*.*') == True)
# print(solution.match_reg_exp('bab', '..*') == True)
# print(solution.match_reg_exp('baba', 'b*.*') == True)
