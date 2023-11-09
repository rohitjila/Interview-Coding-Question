class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for i , j in prerequisites:
            adj[i].append(j)
        visit=set()
        for i in range(numCourses):
                if(self.dfs(i,visit,adj)) == False:
                    return False
        return True
                
    def dfs(self,node,visit,adj):
        if (node in visit):
            return False
        if (adj[node] == []):
            return True
        visit.add(node)
        for it in adj[node]:
            if (self.dfs(it,visit,adj)) == False:
                return False
        visit.remove(node)
        adj[node]=[]
        return True
        
            
            
        
        
        