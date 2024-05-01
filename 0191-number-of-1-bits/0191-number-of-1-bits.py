class Solution:
    def hammingWeight(self, n: int) -> int:
        #  1 0 1 
               # 1
        #brute force
        noOfSetBits = 0
        while(n > 0):
            if(n & 1):
                noOfSetBits +=1
            n = n >> 1  #n // 2
        return noOfSetBits
                
    