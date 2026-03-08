from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        l = 0
        r = len(height) - 1

        left_max = 0
        right_max = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    output += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    output += right_max - height[r]
                r -= 1

        return output


if __name__ == "__main__":
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    # height = [4, 2, 0, 3, 2, 5]
    output = Solution().trap(height)

    print("output", output)
