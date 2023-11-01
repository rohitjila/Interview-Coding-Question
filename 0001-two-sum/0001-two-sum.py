from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp ={}
        for i in range(n):
            a = target - nums[i]
            if (a in mp):
                return [mp[a],i]
            else:
                mp[nums[i]] = i
        
       #brute force
    # [2,7,9,11]
    # target = 9
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if (nums[i] + nums[j] == target):
#                     return [i,j]
                
                
    #better approach 
    # [2,7,9,11]
    #[3,2,4]
    #target = 6
    # target = 9
#     a + b = target
#     a = target - b
#     a = 3
#     b = 3
#     hashmap={2:0 , 7:1 , 9:2 , 11:3}
#     hashmap={3:0 , 2:1 , 4:2}
    # n = len(nums)
    # mp={}
    # for i in range(n):
    #     mp[nums[i]] = i
    # for i in range(n):
    #     a = target - nums[i]
    #     if (a in mp and i != mp[a]):
    #         return [mp[a], i]

    
    #optimal approach 
    # {3:0 ,}
    # [3,3]
    # target = 6
    # a + b = target
    # a = target - b
    
#     n = len(nums)
#         mp ={}
#         for i in range(n):
#             a = target - nums[i]
#             if (a in mp):
#                 return [mp[a],i]
#             else:
#                 mp[nums[i]] = i
    
    
    

        
        