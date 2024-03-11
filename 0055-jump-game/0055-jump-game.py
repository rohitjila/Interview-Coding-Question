class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthestPoint = 0
        for current in range(n):
            if(current > farthestPoint): return False
            farthestPoint = max(current + nums[current], farthestPoint)
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # farthestPoint = 0
        # for current in range(n):
        #     if(farthestPoint < current): return False
        #     farthestPoint = max(current + nums[current],farthestPoint)
        # return True
        