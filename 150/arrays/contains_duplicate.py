from typing import List, Dict


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict.fromkeys(nums)

        if len(hash) != len(nums):
            return True

        return False


if __name__ == "__main__":
    nums = [1, 2, 3]
    output = Solution().hasDuplicate(nums)
    print(output)
