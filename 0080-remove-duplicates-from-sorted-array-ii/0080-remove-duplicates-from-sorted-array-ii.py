class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        for n in nums:
            if(i < 2 or n > nums[i-2]):
                nums[i] = n
                i+=1
        return i
    
       
#kya samjha mai iss problem se length agar 2 rahega to just usko return karna ya duplicate ho ya distinct ho 
#uske baad agar 2 se jyada duplicate value hoga aur hmlog ko value equal to nahi milega tab greater milega
#to uss position wo greater waala number replace ho jayega aur agar bada nahi hai mtlb i-2 duplicate 
#value hai to i wohi ruk jayega kykuki wohi replace karna hai aur jaise hi greater mila hmlog usko
#replace kar diye. 

#T.C --> O(n)
#S.C --> O(1)
        