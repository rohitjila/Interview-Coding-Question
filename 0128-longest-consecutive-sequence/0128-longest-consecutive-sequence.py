class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute better
        s = set(nums)
        mx = 0
        for n in nums:
            if(n-1 not in s):
                length = 0
                while(n + length in s):
                    length += 1
                mx = max(mx,length)
        return mx
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # if(n == 0): return 0
        # #brute force
        # maxCount = 1
        # count = 1
        # nums.sort()
        # for i in range(n-1):
        #     if(nums[i] != nums[i+1]):
        #         if(nums[i]+1 == nums[i+1]):
        #             count +=1
        #         else:
        #             count = 1
        #         maxCount = max(count,maxCount)
        # return maxCount
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # [100,4,200,1,3,2]
        # 1,2,3,4
        # ans= 4
        # brute better
        # longest streak
        # set={100,4,200,1,3,2}
        # [100,4,200,1,3,2]
        # 100 = 1
        # 200 = 1
        # 1 ,2 ,3,4 = 4
        
        # s = set(nums)
        # mx=0
        # for n in nums:
        #     if n-1 not in s:
        #         length=0
        #         while(n + length in s):
        #             length+=1
        #         mx = max(length,mx)
        # return mx
                
        
        
        
        #brute force 
        # 1,2,3,4,100,200
        # maintain longest()
        # 4
#         n = len(nums)
#         if (n == 0):
#             return 0
        
#         nums.sort()
#         cs = 1
#         ls = 1
#         for i in range(n-1):
#             if (nums[i] != nums[i+1]):
#                 if (nums[i]+1 == nums[i+1]):
#                     cs+=1
#                 else:
#                     cs = 1
#                 ls = max(cs,ls)
#         return ls
                
            
        
#             [0,1,1,2]
        
        
        