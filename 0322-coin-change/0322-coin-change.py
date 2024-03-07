class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for i in range(amount+1)] for i in range(n)]
        ind = n - 1
        ans = self.f(coins,ind,amount,dp)
        if(ans == 1e9): return -1
        else: return ans

    def f(self,coins,ind,amount,dp):
        if(ind == 0):
            if(amount % coins[0] == 0): return amount // coins[0]
            else:
                return 1e9
        if(dp[ind][amount] != -1):
            return dp[ind][amount]
        #base case
        #pick
        pick = 1e9
        if(coins[ind] <= amount):
            pick = 1 + self.f(coins,ind,amount-coins[ind],dp)
        #notPick
        notPick = 0 + self.f(coins,ind-1,amount,dp)
        dp[ind][amount] = min(pick,notPick)
        return dp[ind][amount]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# #     def solve(self,ind,coins,target,dp):
# #         if (ind == 0):
# #             if (target % coins[ind] == 0):
# #                 return target // coins[ind]
# #             else:
# #                 return 1e9
# #         if (dp[ind][target] != -1):
# #             return dp[ind][target]
        
# #         nottake = 0 + self.solve(ind-1,coins,target,dp)
# #         take = 999999
# #         if (coins[ind] <= target):
# #             take = 1 + self.solve(ind,coins,target-coins[ind],dp)
# #         dp[ind][target] = min(take,nottake)
# #         return dp[ind][target]

#     def f(self,ind,coins,target,dp):
#         #base case
#         if(ind == 0):
#             if(target % coins[0] == 0): return target // coins[0]
#             else: return 1e9
#         if(dp[ind][target] != 0): return dp[ind][target]

#         notTake = 0 + self.f(ind-1,coins,target,dp)
#         take = 1e9
#         #index will be on same place becuase it is infinite
#         if(coins[ind] <= target):
#             take = 1 + self.f(ind,coins,target - coins[ind],dp)
#         dp[ind][target] = min(take,notTake)
#         return dp[ind][target]
        
#     def coinChange(self, coins: List[int], target: int) -> int:
#         n = len(coins)
#         dp = [[0 for i in range(target+1)] for i in range(n)]
#         #convert memoization into tabulation form
#         for tar in range(0,target+1):
#             if(tar % coins[0] == 0):
#                 dp[0][tar] = tar // coins[0]
#             else:
#                 dp[0][tar] = 1e9
#         #convert the for loop in reverse order
#         for ind in range(1,n):
#             for tar in range(0,target+1):
#                 notTake = 0 + dp[ind-1][tar]
#                 take = 1e9 
#                 #copy paste the recurrence don't think too much
#                 if(coins[ind] <= tar):
#                     take = 1 + dp[ind][tar - coins[ind]]
#                 dp[ind][tar] = min(take,notTake)
#         ans =  dp[n-1][target]

#         # ans =  self.f(n-1,coins,target,dp)
#         if(ans == 1e9): return -1
#         else: return ans

#         # if (target == 0):
#         #     return 0
#         # n = len(coins)
#         # dp = [[0 for i in range(target+1)] for i in range(n)]
#         # for i in range(0,target+1):
#         #     if (i % coins[0] == 0):
#         #         dp[0][i] = i // coins[0]
#         #     else:
#         #         dp[0][i] = 1e9
#         # for i in range(1,n):
#         #     for j in range(1,target+1):
#         #         nottake = 0 + dp[i-1][j]
#         #         take = 1e9
#         #         if (coins[i] <= j):
#         #             take = 1 + dp[i][j-coins[i]]
#         #         dp[i][j] = min(take,nottake)
#         # # print(dp)
            
#         # ans =  dp[n-1][target]
#         # if (ans >= 1e9):
#         #     return -1
#         # else:
#         #     return ans

#         # if (target == 0):
#         #     return 0
#         # n = len(coins)
#         # dp = [[0 for i in range(target+1)] for i in range(n)]
#         # for i in range(0,target+1):
#         #     if (i % coins[0] == 0):
#         #         dp[0][i] = i // coins[0]
#         #     else:
#         #         dp[0][i] = 1e9
#         # for i in range(1,n):
#         #     for j in range(1,target+1):
#         #         nottake = 0 + dp[i-1][j]
#         #         take = 1e9
#         #         if (coins[i] <= j):
#         #             take = 1 + dp[i][j-coins[i]]
#         #         dp[i][j] = min(take,nottake)
#         # # print(dp)
            
#         # ans =  dp[n-1][target]
#         # if (ans >= 1e9):
#         #     return -1
#         # else:
#         #     return ans