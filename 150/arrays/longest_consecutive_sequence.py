from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        high = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                length = 1

                while n + length in nums_set:
                    length += 1

                high = max(length, high)

        return high

    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        nums.sort()
        output = []
        high = 0

        for n in nums:
            if not output:
                output.append(n)
                continue

            last = len(output) - 1

            if output[last] == n:
                continue

            if output[last] + 1 != n:
                high = max(last + 1, high)
                output.clear()
                output.append(n)
                continue

            output.append(n)

        _max = max(high, len(output))
        return _max


if __name__ == "__main__":
    nums = [-1, 0, 1, 0]
    output = Solution().longestConsecutive(nums)
    print("output", output)
