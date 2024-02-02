class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        fo = -1
        lo = -1
        low = 0
        high = n-1
        ans = [-1,-1]
        ans[0] = self.firstOccurence(low,high,target,fo,nums)
        ans[1] = self.lastOccurence(low,high,target,lo,nums)
        return ans
    def firstOccurence(self,low,high,target,fo,nums):
        while(low <= high):
            mid = (low + high) //2
            if(nums[mid] < target):
                low = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                fo = mid
                high = mid - 1
        return fo
    
    
    def lastOccurence(self,low,high,target,lo,nums):
        while(low <= high):
            mid = (low + high) //2
            if(nums[mid] < target):
                low = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                lo = mid
                low = mid + 1
        return lo
        
                
        
                
            
        