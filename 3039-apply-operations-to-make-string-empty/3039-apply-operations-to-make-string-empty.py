class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        count = Counter(s)
        maxCount = max(count.values())
        res = []
        for i in s[::-1]:
            if(count[i] == maxCount):
                res.append(i)
                count[i] -=1
        return "".join(res[::-1])