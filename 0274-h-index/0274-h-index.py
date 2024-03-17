class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #brute force
#         n = len(citations)
#         citations.sort(reverse = True)
#         h = 0

#         for i in range(n):
#             if(citations[i] >= i+1):
#                 h = i+1
#         return h


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
        
        
        