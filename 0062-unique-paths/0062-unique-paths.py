class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for i in range(m)]
        #overlapping subproblem hota hai tab use karte hai
        #no of possible way to reach home
        return self.solve(m-1,n-1,dp)
    
    def solve(self,row,col,dp):
        #base case
        if(row < 0 or col < 0):
            return 0
        if(row == 0 and col == 0):
            return 1
        
        if(dp[row][col] != -1):
            return dp[row][col]
        #actual logic
        dp[row][col] =  self.solve(row-1,col,dp) + self.solve(row,col-1,dp)
        return dp[row][col]
    
    
    
  
        


        
        

















        