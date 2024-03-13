class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        n = len(prices)

        for i in range(n):
            if(prices[i] < mn):
                mn = prices[i]
            ans = max(prices[i] - mn , ans)
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # profit = 0
        # minimum = a[0]
        # n = len(a)
        # for i in range(n):
        #     if(a[i] > minimum):
        #         profit = max(profit,a[i]-minimum)
        #     else:
        #         minimum=a[i]
        # return profit
        