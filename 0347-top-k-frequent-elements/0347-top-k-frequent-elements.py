class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,2,3]
        # {1:3 , 2:2 , 3:1}
        #[[3,1],[2,2][1,3]]
        # sort the array according to frequency 
        # for i in range(k):
        arr=[]
        mp = collections.defaultdict(lambda : 0)
        for i in range(len(nums)):
            mp[nums[i]]+=1
        for i in mp:
            arr.append([mp[i],i])
        arr.sort(reverse = True)
        ans=[]
        for i in range(k):
            ans.append(arr[i][1])
        return ans
            
    # Time Complexity - O(2n)+O(nlog(n))+ O(k)
    # Space Complexity - O(3n)
    
            
        
            
        
        
