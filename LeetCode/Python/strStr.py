# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1

        if haystack == needle:
            return 0

        for i in range(len(haystack)):
            k = i
            for char in needle:
                if char != haystack[k]:
                    break

                if char == haystack[k]:
                    k += 1

                if k - i == len(needle):
                    return i

                if k == len(haystack):
                    break

        return -1
