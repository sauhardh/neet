from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]

            print(s)
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

        return []


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    target = 3
    output = Solution().twoSum(numbers, target)
    print("output", output)
