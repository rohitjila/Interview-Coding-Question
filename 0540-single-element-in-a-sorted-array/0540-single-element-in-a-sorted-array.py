#sabse pehle kya karna hai best answer ke liye observe karna hai pehla ki single element hai wo hamesha even index pe hai usse left me jo duplicate hai wo hamesha even and odd ka pattern follow kar rahe hai hai uske right me odd and even ka pattern ka follow kar rahe hai to hmklog ko mid hamesha even index pe rakhna hai taaki hmlog check kar sake ki kaha hai hmlog right side ya left side me okay right me hoga to right = mid kar denge kyuki hmlog damn sure ho jayenge ki right me value nahi hai kyuki yaha odd even ka pattern follow ho raha hai aur jab left me hoga to left = mid + 2 kar denge kyuki pata even odd dono barabar hai to uske baad hi hoga jab tak loop chal raha hai chalao answer nums[left] me hoga kyuki hamesha left = mid + 2 aur jaha last me rukega wohi single element hoga jab last me ye rukega tab
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while(left < right):
            mid = (left + right ) // 2
            if(mid % 2 == 1):
                mid -= 1
            if(nums[mid] == nums[mid+1]):
                left = mid + 2
            else:
                right = mid
        return nums[left]

        