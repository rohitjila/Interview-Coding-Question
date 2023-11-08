class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #count how many rotten oranges are there
        #count the fresh oranges as we have to decrement once we made them rotten
        queue = deque()
        fresh,time=0,0
        ROWS,COLS=len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == 2):
                    queue.append([i,j])
                if (grid[i][j] == 1):
                    fresh+=1
        #if there is rotten oranges in queue and fresh oranges are more than 
        #zero then we will use bfs to make then rotten
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        while(fresh > 0 and queue):
            for i in range(len(queue)):
                r,c=queue.popleft()
                #here we will check the boundaries condition
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if (row < 0 or col < 0 or row == len(grid) 
                       or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row,col])
                    fresh-=1
            time+=1
        if (fresh == 0):
            return time
        else:
            return -1
        