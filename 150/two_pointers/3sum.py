from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[l] + nums[r] + nums[i]

                if s == 0:
                    print(output)
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        continue
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return output


if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    output = Solution().threeSum(nums)
    print("output", output)
