import sys
sys.setrecursionlimit(10**6)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c= len(grid) , len(grid[0])
        visit=set()
        area=0
        for i in range(r):
            for j in range(c):
                area=max(area,self.dfs(i,j,grid,r,c,visit))
        return area
    
    def dfs(self,i,j,grid,r,c,visit):
        if (i < 0 or j < 0 or i == r or j == c 
              or grid[i][j] == 0 or (i,j) in visit):
            return 0
            
        visit.add((i,j))
        return (1+self.dfs(i+1,j,grid,r,c,visit)+
                self.dfs(i-1,j,grid,r,c,visit)+
                self.dfs(i,j-1,grid,r,c,visit)+
                self.dfs(i,j+1,grid,r,c,visit))
        
        
        
        