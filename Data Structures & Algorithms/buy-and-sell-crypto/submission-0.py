class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        minBuy = prices[0]

        for sell in prices:
            maxi = max(maxi, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxi