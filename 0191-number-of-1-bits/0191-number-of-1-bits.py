class Solution:
    def hammingWeight(self, n: int) -> int:
        #Brute force approach
        # count = 0
        # while(n > 0):
        #     if (n & 1):
        #         count+=1
        #     n = n >> 1
        # return count
    
        #brute better approach
        count = 0
        while(n):
            n &= n-1
            count+=1
        return count
    
    
    
    
#time complexity ->32 , 16 , 8 , 4 , 2 , 1, 0
# O(logn)
# O(1)=> Space Complexity
#           0 0 1   => 5   & 
#              &1
#     ------------
#             1
#         5 >> 1
#         5 // 2 = 2
#         2 >> 1
#         2 // 2 = 1
#         1 >> 1
#         1 // 2 = 0
        
#         count +=1
#         count = 2