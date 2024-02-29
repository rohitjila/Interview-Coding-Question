#Isme kar kya rahe hai ki sabse pehle hmlog set me har ek number ka prefix daal rahe hai jaise ki 
#maan lo 123 hai to uska prefix ho jayega 1 12 123 ye set me hai abb hmlog arr2 me jayenge aur check
#karenge ki wo prefix present hai ki nahi set me har ek number ka iss tarah se koi bhi number
#ka mil prefix mil jata uss number ka kaam khatam kar dete.
class Solution:
    def length(self,n):
        ans = str(n)
        return len(ans)
    
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        maxi = 0
        s =  set()
        for n in arr1:
            while(n > 0):
                s.add(n)
                n //=10
                
        for m in arr2:
            while(m > 0):
                if(m in s):
                    maxi = max(maxi,self.length(m))
                    break
                m //=10
        return maxi
            
                
        
                
                

    
        
            
            
        
        