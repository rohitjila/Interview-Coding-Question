class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #brute force method is just count each number and check whether the number is greater than
        #n // 2 if yes the return the major element
        #we can do this by hashing 
        #if there is 100 percent chance that majority element exist then simply sort the array and return 
        #n // 2 index value because till that position majority element will be occupied.
        
        #brute better(Moore voting algorithm)
        expectedMajorityElement = nums[0]
        count = 0
        n = len(nums)
        for i in range(0,n):
            if(count == 0):
                expectedMajorityElement = nums[i] 
            if(nums[i] == expectedMajorityElement):
                count +=1
            elif(nums[i] != expectedMajorityElement):
                count-=1
                if(count <= 0):
                    count = 0
        return expectedMajorityElement
        
            
            
        
