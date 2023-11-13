class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for i in range(numCourses)]
        for i , j in prerequisites:
            adj[i].append(j)
        visit=set()
        
        ans1=[]
        ans=[]
        # for i in ans:
        #     if i not in ans1:
        #         ans1.append(i)
        
        flag = 0
        for i in range(numCourses):
            if (self.dfs(i,adj,visit,ans)) == False:
                flag = 1
        if (flag == 1):
            return []
        else:
            for i in ans:
                if i not in ans1:
                    ans1.append(i)
            return ans1
        
        
    def dfs(self,node,adj,visit,ans):
        if node in visit:
            return False
        if (adj[node] == []):
            ans.append(node)
            return True
        
        visit.add(node)
        for it in adj[node]:
            if (self.dfs(it,adj,visit,ans)) == False:
                return False
        visit.remove(node)
        adj[node] = []
        ans.append(node)
        return True
        
        