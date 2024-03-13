class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)] for i in range(n)]
        return self.f(0,1,prices,n,dp)
    
    def f(self,ind,buy,prices,n,dp):
        if(ind == n):
            return 0
        if(dp[ind][buy] != -1):
            return dp[ind][buy]
        if(buy):
            profit = max((-prices[ind] + self.f(ind+1,0,prices,n,dp)) , self.f(ind+1,1,prices,n,dp))
        else:
            profit = max((prices[ind] + self.f(ind+1,1,prices,n,dp)) , self.f(ind+1,0,prices,n,dp))
        dp[ind][buy] = profit
        return dp[ind][buy]
            
            
