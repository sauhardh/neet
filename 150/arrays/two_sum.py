from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums[(i + 1) :]:
                pos = nums.index(diff, i + 1)
                return [i, pos]

        return []


if __name__ == "__main__":
    nums = [3, 4, 5, 6]
    target = 7
    output = Solution().twoSum(nums, target)
    print("output", output)
