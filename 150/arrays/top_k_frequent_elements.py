from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in counts[:k]]


if __name__ == "__main__":
    nums = [1, 2]
    k = 2
    output = Solution().topKFrequent(nums, k)
    print("output", output)
