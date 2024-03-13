class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(2)] for i in range(n+1)]
        #base case
        
        for ind in range(n-1,-1,-1):
            for buy in range(0,2):
                if(buy):
                    profit = max(-prices[ind] + dp[ind+1][0],dp[ind+1][1])
                else:
                    profit = max(prices[ind] + dp[ind+1][1], dp[ind+1][0])
                dp[ind][buy] =  profit
        return dp[ind][buy]
                
        # return self.f(0,1,prices,n,dp)
    
    # def f(self,ind,buy,prices,n,dp):
    #     if(ind == n):
    #         return 0
    #     if(dp[ind][buy] != -1):
    #         return dp[ind][buy]
    #     if(buy):
    #         profit = max((-prices[ind] + self.f(ind+1,0,prices,n,dp)) , self.f(ind+1,1,prices,n,dp))
    #     else:
    #         profit = max((prices[ind] + self.f(ind+1,1,prices,n,dp)) , self.f(ind+1,0,prices,n,dp))
    #     dp[ind][buy] = profit
    #     return dp[ind][buy]
            
            
