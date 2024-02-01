from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mp = defaultdict(lambda : 0)
        count = 0
        for i in nums:
            if(i + k in mp):
                count += mp[i + k]
            if(i - k in mp):
                count += mp[i-k]
            mp[i] += 1
        return count
            
        