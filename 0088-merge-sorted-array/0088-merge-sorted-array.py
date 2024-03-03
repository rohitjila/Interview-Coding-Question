class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while(m and n):
            if(nums2[n-1] > nums1[m-1]):
                nums1[m+n-1] = nums2[n-1]
                n -=1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -=1
                
        while(n):
            nums1[m+n-1] = nums2[n-1]
            n -=1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force yaha pe kuch nahi kar rahe hai bas second array ka element first element me
        #lagane ke baad sort kar de rahe hai
        #time complexity -> O(m+n) * log(m+n)
        #space complexity -> O(1)
        # for j in range(n):
        #     nums1[m+j] = nums2[j]
        # nums1.sort()
        
        #brute better
        #yaha pe kya karna hai compare karna ka hi kon bada number hai dono array me aur piche se 
        #arrange karte aana hai
        #T.C : O(m + n)
        #S.C : O(1)
        # while(m > 0 and n > 0):
        #     if(nums1[m-1] > nums2[n-1]):
        #         nums1[m+n-1] = nums1[m-1]
        #         m-=1
        #     else:
        #         nums1[m+n-1] = nums2[n-1]
        #         n-=1
        # #iska yahi mltb hai ki jab m=0 hai to saara value n ka m me append kar dena hai.   
        # while(n > 0):
        #     nums1[n-1] = nums2[n-1]
        #     n-=1
    
            
            
            
            
        