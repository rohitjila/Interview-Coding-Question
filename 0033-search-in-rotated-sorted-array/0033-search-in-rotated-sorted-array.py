#            check the mid is lying in which sequence 1st increasing sequence or 2nd increasing sequence
#            and we always know ki 2nd increasing sequence hamesha 1st increasing sequence se chota hota hai
#            kyuki jab bhi sort karenge to 2nd increasing sequence pehle aayega tab first aayega
                # it means mid mera 1st increasung sequence me hai #abb check karna ki target mera iss sequence me                   karta hai ya nahi aur agar target first number se chota ya phir ya phir target mera mid se bara means 
#              wo second sequence me hai and vice versa karna hai else condition agar answer mil jaye to mid return kar do warna -1 return kar do agar nahi mile to
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while(low <= high):
            mid = (low + high) //2
            if(nums[mid] == target): return mid
            if(nums[mid] >= nums[0]):
                if(target < nums[0] or target > nums[mid]): low = mid+1
                else: high = mid - 1
            else:
                if(target > nums[n-1] or target < nums[mid]): high = mid-1
                else: low = mid + 1
        return -1
                
            
        
                
             
                
        
        