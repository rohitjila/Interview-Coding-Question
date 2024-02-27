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
                
        