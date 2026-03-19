from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


if __name__ == "__main__":
    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]
    output = Solution().carFleet(target, position, speed)
    print("Output", output)
