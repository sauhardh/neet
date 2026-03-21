from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, (i - idx) * height)
                start = idx
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


if __name__ == "__main__":
    heights = [7, 1, 7, 2, 2, 4]
    output = Solution().largestRectangleArea(heights)
    print("Output", output)
