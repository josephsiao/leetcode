from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 0
        sell_price = 0
        i = 0
        ans = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy_price = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell_price = prices[i]
            ans += sell_price - buy_price

        return ans


if __name__ == "__main__":
    try:
        Solution = Solution()
        prices = [1, 2, 3, 4, 5]
        print(Solution.maxProfit(prices))
    except Exception as e:
        print(e)
    finally:
        pass
