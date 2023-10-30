"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""




#steps to follow clone a graph

#visited array where we will store the address of each node
#we will do simple dfs to copy that array
class Solution:
    def dfs(self,node,copy,vis):
        #first thing jo hmlog ko karna hai wo jo actual node ka value
        #hai waha pe copy waale node ka address daal dena hai kyuki
        #hmlog check kar sake hai ki agar copy alrady created hai
        #to simple copy waale node me directly add kar denge
        vis[node.val] = copy
        for it in node.neighbors:
            #hmlog ko sabse pehle check karna hai jo actual node
            #ka neighbor hai wo already visited to nahi hai
            if(vis[it.val] == None):
                #tab yaha pe newnode create karlo aur uske 
                #nieghbors me add kar do
                newNode = Node(it.val)
                copy.neighbors.append(newNode)
                self.dfs(it,newNode,vis)
            else:
                #agar wo already visited hai to simply push kar do
                copy.neighbors.append(vis[it.val])
                
                
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        vis = [None] * 101 
        #Yaha hmlog copy node create kar rahe hai 
        copy = Node(node.val)
        self.dfs(node,copy,vis)
        return copy





















        # if (node == None):
        #     return 
        # vis = [None]*(101)
        # copy = Node(node.val)
        # self.dfs(node,copy,vis)
        # return copy
        