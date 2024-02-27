class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        for i in range(2,n):
            if(nums[i] == nums[i-2]): return False
        return True
        