class Solution:
    def isPrefixAndSuffix(self,str1,str2):
        length1 = len(str1)
        if(str1[:length1] == str2[:length1] and str1[:length1] == str2[-length1:]):
            return True
        else:
            return False
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if(self.isPrefixAndSuffix(words[i],words[j]) == True):
                    count +=1
        return count
        