class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        while(j < n):
            if(nums[j] != val):
                nums[i] = nums[j]
                i+=1
            j+=1
        return i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
    
       #same approach hai dekho kon sa element ko remove nahi karna hai
       #usko aage kardo aur ek pointer se update karo jo number ko remove nahi karna hai
       #wo peeche reh jayega hmlog ka index wohi tak point karega jo number ko consider
       #karna hai.
    
      # T.C -> O(n)
      # S.C --> O(1)
        