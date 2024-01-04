class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        mx = 0
        st = set()
        for r in range(len(s)):
            while(l < r and s[r] in st):
                st.remove(s[l])
                l+=1
            st.add(s[r])
            
            mx = max(mx,r-l+1)
        return mx
#         i = 0
#         j = 0 
#         mp = collections.defaultdict(lambda : 0)
#         ans = 0
#         while(j < len(s)):
#             mp[s[j]]+=1
#             if(len(mp) == j-i+1):
#                 ans = max(ans,len(mp))
                
#             if (len(mp) < j-i+1):
#                 while(len(mp) < j-i+1):
#                     mp[s[i]]-=1
#                     # if (mp[s[i]] == 0):
#                     #     del[mp[s[i]]]
#                     i+=1
            
#             j+=1
#         return ans
                
                
            
                
            
            
        