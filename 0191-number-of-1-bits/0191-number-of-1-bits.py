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
    
#Let num be 25 (binary: 11001). In the first iteration, we flip the rightmost set bit (position 0), and count becomes 1. In the next iteration, we flip the next rightmost set bit (position 3), and count becomes 2. We continue until there are no more set bits, and the final count is 3. So, there are 3 set bits in the binary representation of 25.This leads to time complexity O(k) k is representing  where K is the number of set bits in the binary representation of the input number.

    
    
    
    
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