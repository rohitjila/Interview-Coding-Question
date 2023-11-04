class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(height) , len(height[0])
        pac,atl = set() , set()
        
        def dfs(r,c,visit,prevHeight):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or
              height[r][c] < prevHeight or (r,c) in visit):
                return
            visit.add((r,c))
            
            dfs(r+1,c,visit,height[r][c])
            dfs(r-1,c,visit,height[r][c])
            dfs(r,c+1,visit,height[r][c])
            dfs(r,c-1,visit,height[r][c])
            
        
        for c in range(COLS):
            dfs(0,c,pac,height[0][c])
            dfs(ROWS-1,c,atl,height[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r,0,pac,height[r][0])
            dfs(r,COLS-1,atl,height[r][COLS-1])
            
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if(r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
