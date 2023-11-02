from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sorting 
        # [1,2,3,1]
        # after sort 
        # [1,2,3]
        # return false
        #time complexity ->O(nlogn) + O(n) -> O(nlogn) 
        #space complexity -> O(1)
        # n = len(nums)
        # nums.sort()
        # for i in range(n-1):
        #     if (nums[i] == nums[i+1]):
        #         return True
        # return False
        
    
    
    
        #hashing method
        # [1,2,3,1]  -> 
        #[1,2,3]
#         frequency count of each values
#         {1 : 1 , 2 : 1 , 3: 1}
#         return false
        
#         Time complexity -> O(n) + O(n) => O(2n)
#         Space Complexity ->O(n)
        mp = defaultdict(lambda : 0)
        for i in range(len(nums)):
            mp[nums[i]]+=1
            
        for i in mp:
            if (mp[i] >= 2):
                return True
        return False
            


        
        
        
        
        
    