class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #brute force
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
    
        #brute better
        n = len(nums)
        index = 0
        for i in range(n):
            if(nums[i] != val):
                nums[index] = nums[i]
                index+=1
        return index
        