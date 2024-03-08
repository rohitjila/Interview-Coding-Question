class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        while(mid <= high):
            if(nums[mid] == 0):
                nums[low],nums[mid] = nums[mid],nums[low]
                low +=1
                mid +=1
            elif(nums[mid] == 2):
                nums[high],nums[mid] = nums[mid],nums[high]
                high-=1
            else:
                mid+=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #brute force
#         #t.c = O(n)
#         #s.c = O(1)
#         #why this is brute force because here we are using 2 loops and in optimal solution is using 
#         #1 loops. Having same time complexity and space complexity.
        
#         n = len(arr)
# #         count0 = 0
# #         count1 = 0
# #         count2 = 0
# #         for i in range(n):
# #             if(arr[i] == 0):
# #                 count0 +=1 
# #             elif(arr[i] == 1):
# #                 count1+=1
# #             else:
# #                 count2 +=1
          
# #         i = 0
# #         while(i < n):
# #             while(count0):
# #                 arr[i] = 0
# #                 count0 -=1
# #                 i+=1
                
# #             while(count1):
# #                 arr[i] = 1
# #                 count1 -=1
# #                 i+=1
                
# #             while(count2):
# #                 arr[i] = 2
# #                 count2 -=1
# #                 i+=1
                
        
        
            
#         #brute better  
            
#         low = 0
#         mid = 0
#         high = n-1
#         while(mid < high):
#             if (arr[mid] == 0):
#                 arr[low],arr[mid]=arr[mid],arr[low]
#                 low+=1
#                 mid+=1
#             elif(arr[mid] == 1):
#                 mid+=1
#             elif(arr[mid] == 2):
#                 arr[mid],arr[high]=arr[high],arr[mid]
#                 high-=1
        