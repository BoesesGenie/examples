# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        result = strs[0]

        for i in range(len(strs)):
            if strs[i].startswith(result):
                continue
            else:
                while len(result):
                    result = result[:-1]

                    if strs[i].startswith(result):
                        break
                    elif result == '':
                        return ''

        return result


solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))