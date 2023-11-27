class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l,r=0,len(arr)-1
        while(l < r):
            if (arr[l] + arr[r]) > target:
                r-=1
            if (arr[l] + arr[r]) < target:
                l+=1
            elif(arr[l] + arr[r]) == target:
                return [l+1,r+1]
        