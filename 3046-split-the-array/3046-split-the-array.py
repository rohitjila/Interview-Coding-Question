from collections import defaultdict
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        # nums.sort()
        # for i in range(2,n):
        #     if(nums[i] == nums[i-2]): return False
        # return True
    
        #the basic idea is to check if the frequency is more than 2 it means we can't take distinct value
        #in both the array
        
        #brute force
        #t.c -> O(nlog(n) + O(n))
        #s.c -> O(1)
        
        #brute better
        
        mp = defaultdict(lambda : 0)
        for i  in range(n):
            mp[nums[i]] += 1
        for i in mp:
            if(mp[i] > 2): return False
        return True
      
        #t.c => O(n)
        #s.c => O(1)
        
        
    
        