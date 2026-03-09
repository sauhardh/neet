from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_till_now = 0

        for i, price in enumerate(prices):
            if i == 0 or min_till_now > price:
                min_till_now = price
                continue

            profit = max(price - min_till_now, profit)

        return profit


if __name__ == "__main__":
    # prices = [10, 1, 5, 6, 7, 1]
    # prices = [10, 8, 7, 5, 2]
    # prices = [5, 1, 5, 6, 7, 1, 10]
    # prices = [2, 1]

    # prices = [3, 4, 1]

    prices = [3, 2, 6, 5, 0, 3]

    output = Solution().maxProfit(prices)
    print("output", output)
