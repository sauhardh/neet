from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        highest = 0
        while l < r:
            height = min(heights[r], heights[l])
            width = abs(r - l)
            area = height * width

            highest = max(area, highest)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return highest


if __name__ == "__main__":
    # heights = [1, 7, 2, 5, 4, 7, 3, 6]
    heights = [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 7, 3, 6]
    output = Solution().maxArea(heights)
    print("output", output)
