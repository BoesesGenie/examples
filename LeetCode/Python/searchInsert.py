# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                return mid

        return mid + 1 if nums[mid] < target else mid
