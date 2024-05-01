class Solution:
    def hammingWeight(self, n: int) -> int:
        #brute better
        #1 0 1 1
        #1 0 1 0     
        count = 0
        while(n):
            n = n & n - 1
            count +=1
        return count
                
                
    