from typing import List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # prefix
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output

    def productExceptSelfSlow(self, nums: List[int]) -> List[int]:
        output = []
        for i, _ in enumerate(nums):
            prefix = prod(nums[:i])
            suffix = prod(nums[i + 1 :])

            output.append(prefix * suffix)

        return output


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, 3]
    nums = [1, 2, 4, 6]
    print("input", nums)
    output = Solution().productExceptSelf(nums)
    print("output", output)
