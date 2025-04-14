# https://leetcode.com/problems/4sum/
# NB: the algorithm can be optimized!

class Solution(object):
    def fourSum(self, nums, target):
        result = set()

        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1

                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if current_sum == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))

                    if current_sum < target:
                        k = k + 1
                    else:
                        l = l - 1

        return list(map(lambda item : list(item), result))

solution = Solution()

print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
print(solution.fourSum([2, 2, 2, 2, 2], 8))