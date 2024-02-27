class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        area = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i+1,n):
                minX = max(bottomLeft[i][0],bottomLeft[j][0])
                maxX = min(topRight[i][0],topRight[j][0])
                minY = max(bottomLeft[i][1],bottomLeft[j][1])
                maxY = min(topRight[i][1],topRight[j][1])
                
                if(minX < maxX and minY < maxY):
                    side = min(maxX - minX,maxY - minY)
                    area = max(area,side*side)
        return area
    
    
#     Isme sabse pehle kya karna tha ki intersection nikalna tha aur uske liye jo formula hota hai
#     kabhi bhi intersection nikalna ho to line 7 - 10 of code hai aur excel sheet me maintained hai
#     hai ki kaise nikale phir hmlog check kiye ki kya ye rectangle form kar raha hai ki nahi
#     agar manlo maxX co-ordinate minX se bada ho jaye to ye valid nahi hai to agar valid hoga 
#     tabhi rectangle hoga phir rectangle ka min side nikal le lenge kyuki usi ka side ka square 
#     banega aur phir hmlog area of square calculate kar lenge thik aur pure array me jo maximum
#     area of square hoga usko return kar denge.
                
        