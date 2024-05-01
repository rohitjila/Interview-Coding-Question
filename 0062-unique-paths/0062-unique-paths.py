class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Most brute method
        #Yaha kya karna hai observation ki if answer 3 hai to m column hai to m - 1 utna baar right aayega hi
        #agar n row hai to utna baar down aayega hi. R R D two R chune to ek D aayega hi ,  R D R , D R R
        #isliye maxiumm yaha to m -1 ya n -1 ka combination banega total ke saath that is m + n - 2 ke saath
        #overall observation hai ki m - 1 + n - 1 isko chalna hi chalna hai kitne tarike wo pahuch sakta hai
        #wo combination se pata chalega
        
        #T.C : O(m-1)  , O(n-1)
        #S.C : O(1)
        
        N = m + n -2
        r = m - 1
        res = 1
        for i in range(1,r+1):
            res = res *  (N -i + 1) // i
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dp = [[0 for i in range(n)] for i in range(m)]
        # for row in range(0,m):
        #     for col in range(0,n):
        #         #base case
        #         if(row == 0 and col == 0):
        #             dp[0][0] = 1
        #         else:
        #             up = 0
        #             left = 0
        #             if(row > 0):
        #                 up = dp[row-1][col]
        #             if(col > 0):
        #                 left = dp[row][col-1]
        #             dp[row][col] = up + left
        # return dp[m-1][n-1]

        # return self.solve(m-1,n-1,dp)
        # finish se staring tak jaa rahe hai
        #down - up
        #right - left
        #memoization
        #dp declare karna padta hai
        #Tabulation
        #base case
        #for loop me jo main function hai usko likho
        #copy paste karo recurrence

    # def solve(self,row,col,dp):
    #     #base case
    #     if(row < 0 or col < 0):  #home se bahar
    #         return 0
    #     if(row == 0 and col == 0):  #home 
    #         return 1

    #     #memoization
    #     if(dp[row][col] != -1):
    #         return dp[row][col]

    #     #main body
    #     up = self.solve(row-1,col,dp)
    #     left = self.solve(row,col-1,dp)

    #     #return statement
    #     dp[row][col] =  up + left
    #     return dp[row][col]


        # T.C-> O(2 ^ (n*m))  O(n * m)  --> O(n * m)
        # A.S.C --> O(n + m)---> O(n + m) --> O(1)
        # S.C -->               O(n*m)    O(n * m)



        
        

















        