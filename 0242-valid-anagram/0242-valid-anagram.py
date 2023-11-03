from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #cat and atc
        # c : 1 a : 1 t: 1
        
        #1st method 
        #sort act act
        #true
        #O(nlogn) + O(nlogn)
#         if (len(s) != len(t)):
#             return False
#         s = list(s)
#         s.sort()
        
#         t = list(t)
#         t.sort()
        
#         if (s == t):
#             return True
#         else:
#             return False
        
        #2nd method
         # c : 1 a : 1 t: 1
          # c : 1 a : 1 t: 1
        #O(n) + O(n)
        #O(n) + O(n)
        
        mp = defaultdict(lambda : 0)
        mp1 = defaultdict(lambda : 0)
        for i in s:
            mp[i]+=1
        for i in t:
            mp1[i]+=1
        if (mp == mp1):
            return True
        else:
            return False
            
        
        
        
        