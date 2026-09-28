class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy once, sell once afterwards
        # 1) 2 pointers i (buy) & j (sell)
        # if p[i] > p[j] -> better point to buy: j = i; i += 1
        # profit = p[j] - p[i]
        # maxprofit = max(profit, maxprofit)
        # j += 1
        # return maxprofit

        buy = 0
        profit = 0
        maxprofit = 0

        for sell in range(len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
                continue
            profit = prices[sell] - prices[buy]
            maxprofit = max(profit, maxprofit)
        return maxprofit
        