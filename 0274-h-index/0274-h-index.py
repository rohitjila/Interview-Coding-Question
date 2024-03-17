#Isme ek tarika hai ki sort kardo reverse order me jisme hoga kya ki hmlog check kar sakte hai ki 
#number of paper jis samay less than ho gaya uske pehle waala index answer hoga kyuki waha tak index
#or uska paer equal to ya barabar hai to usse pehle waala bhi bada hi hoga

#brute better me kya hoga ki hmko pata hai ki maximum h-index hoga wo length of array ke barabar hoga
#tp count karo ki kitna paper citate hua hai uska count badha do aur length of array se bada hai to usi
#last index pe count badha do #phir reverse way me count karo ki kitna paper citate hua hai agar uss index
#ya usse bada ko count to i return kar do means yahi answer hai jo bata raha hai ki itna ya isse
#jyada index tak paper citate hua hai.


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #brute better
        #S.C => O(n(log(n)))
        #T.C => O(1)
        #brute force
#         n = len(citations)
#         citations.sort(reverse = True)
#         h = 0

#         for i in range(n):
#             if(citations[i] >= i+1):
#                 h = i+1
#         return h

        #brute better
        #S.C => O(n)
        #T.C => O(n)
        n = len(citations)
        arr = [0] * (n + 1)
        for c in citations:
            if(c > n):
                arr[n] +=1
            else:
                arr[c] +=1
                
        count = 0
        for i in range(n,-1,-1):
            count += arr[i]
            if(count >= i):
                return i
        
        
        