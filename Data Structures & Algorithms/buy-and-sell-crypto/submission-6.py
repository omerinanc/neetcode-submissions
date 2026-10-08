class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if profit < (prices[len(prices) - 1 - i]) - prices[j] and len(prices) - 1 - i > j:
                    profit = (prices[len(prices) - 1 - i]) - prices[j]
                    print(profit)
        return profit