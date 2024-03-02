class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farest = 0
        for i in range(n):
            if(farest < i): return False
            farest = max(i + nums[i], farest)
        return True
        