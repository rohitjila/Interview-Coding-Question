class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current = 0
        jumps = 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest,nums[i] + i)
            if(i == current):
                current = farthest
                jumps+=1
        return jumps
        