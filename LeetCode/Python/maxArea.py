class Solution(object):
    def maxArea(self, height):
        max_product = 0
        i, j = 0, len(height) - 1
        max_height = 0

        while i < j:
            if height[i] > max_height and height[j] > max_height:
                max_height = min(height[i], height[j])
                max_product = max(max_height * (j - i), max_product)

            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -=1

        return max_product
