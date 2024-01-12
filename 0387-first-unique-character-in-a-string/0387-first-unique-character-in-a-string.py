from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        mp = defaultdict(lambda : 0)
        for i in range(len(s)):
            mp[s[i]] +=1
        for i in range(len(s)):
            if(mp[s[i]] == 1):
                ans = i
                break
        return ans
                