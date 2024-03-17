class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverse(0,len(nums)-1,nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,len(nums)-1,nums)
    
    def reverse(self,start,end,nums):
        while(start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start+=1
            end-=1
            
        
        