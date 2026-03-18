from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        st = []

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                output[idx] = i - idx

            st.append(i)

        return output


if __name__ == "__main__":
    # output = [1, 4, 1, 2, 1, 0, 0]
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    output = Solution().dailyTemperatures(temperatures)
    print("Output", output)
