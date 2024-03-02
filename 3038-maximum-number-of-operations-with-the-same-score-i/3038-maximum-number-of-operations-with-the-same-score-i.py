class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        Sum = nums[0] + nums[1]
        for i in range(2,n-1,2):
            if(Sum == nums[i] + nums[i+1]):
                count +=1
            else:
                break
        return count
        

        
            
            
        