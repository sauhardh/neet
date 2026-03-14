from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()

        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                output.append(nums[dq[0]])

        return output


if __name__ == "__main__":
    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    output = Solution().maxSlidingWindow(nums, k)
    print("output", output)


"""

    def maxSlidingWindowSlow(self, nums: List[int], k: int) -> List[int]:
        max_values = []

        l = 0
        r = k

        while r <= len(nums):
            m = max(nums[l:r])
            max_values.append(m)

            l += 1
            r += 1

        return max_values



"""
