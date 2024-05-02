class Solution:
    def hammingWeight(self, n: int) -> int:
      # 16  8  4  2  1 
      # 1   0  0  0  1
      # 1   0   0 0  0
      #   #brute better
      #   #1 0 1 1
      #   #1 0 1 0
      #   #-------------------
      #    1  0  1  0
      #    1  0  0  1
      #   ------------
      #   1   0   0  0
      #   0  0   0   1
      #   --------------
      #   0  0  0    0
        
      #T.C --> O(k)
      #S.C --> O(1)
        
        count = 0 
        while(n):
            n = n & n - 1
            count +=1
        return count
                
                
    