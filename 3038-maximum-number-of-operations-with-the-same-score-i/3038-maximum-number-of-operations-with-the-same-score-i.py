class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 1
        n = len(nums)
        Sum = 0
        if(n % 2 == 0):
            for i in range(0,n-1,2):
                prevSum = Sum
                Sum = nums[i] + nums[i+1]
                if(i != 0):
                    if(Sum == prevSum):
                        count +=1
                    else:
                        break
        else:
            for i in range(0,n-1,2):
                prevSum = Sum
                Sum = nums[i] + nums[i+1]
                if(i != 0):
                    if(Sum == prevSum):
                        count +=1
                    else:
                        break
        return count
        
        

        
            
            
        