# https://leetcode.com/problems/3sum-closest/
# NB: the algorithm can be optimized!

class Solution(object):
    def threeSumClosest(self, nums, target):
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        diff = abs(result - target)

        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == target:
                    return current_sum

                current_diff = abs(current_sum - target)

                if diff > current_diff:
                    diff = current_diff
                    result = current_sum

                if current_sum < target:
                    j = j + 1
                else:
                    k = k - 1

        return result

solution = Solution()

print(solution.threeSumClosest([-1,2,1,-4], 1))
print(solution.threeSumClosest([0,0,0], 1))
print(solution.threeSumClosest([2, 5, 6, 7], 16))