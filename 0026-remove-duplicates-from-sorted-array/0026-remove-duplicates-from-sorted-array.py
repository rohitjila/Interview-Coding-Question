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
        
        #time complexity --> O(n)
        #space complexitty --> O(1)
        
        #let's see basically isme kaise ho raha hai 
        #example le lo arr=[0,0,1,1,1]
        # i = 0
        #J = 1
        #to yaha hmlog check kar rahe hai ki to value match nahi kiya it means wo duplicate nahi 
        #hai to ek step i ka aage badha do waha pe unique value ko place kar do
        #or jo duplicate hai usko ignore kar do
        #dry run 
        #arr[i] == arr[j] hai sidha j+=1 kar denge phir agla step me i =0j = 2 pe hai
        #waha 1 != 0 ho gaya to abb i ka value aage badha ke 1 ko waha put kar denge
        # phir j 2 pe hai i 1 pe hai to duplicate jo aage badha denge phir j=3 ho jayega index
        # 3 aur 1 same hai to j aage badh jaayega to loop khatam aur hmlog answer return kar denge
            
        