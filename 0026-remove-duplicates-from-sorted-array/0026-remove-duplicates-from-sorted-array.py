class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = 1
        while(j < n):
            if(arr[i] != arr[j]):
                i+=1
                arr[i] = arr[j]
            j+=1
        return i+1
                
            
        