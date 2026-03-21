from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(left, right):
            mid = int((left + right) / 2)
            if left > right:
                return -1

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)

        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    # nums = [-1, 0, 2, 3, 4, 6, 8]
    # target = 4
    nums = [-1, 0, 2, 4, 6, 8]
    target = 3
    output = Solution().search(nums, target)
    print("Output", output)
