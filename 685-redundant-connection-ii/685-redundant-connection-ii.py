class UnionFind:
    
    def __init__(self):
        self.parent = {}
    
    def find(self,x):
        
        while x != self.parent.get(x,x):
            x = self.parent.get(x,x)
        
        return x
        
    def union(self,x,y):
        
        parentx = self.find(x)
        parenty = self.find(y)
        
        if parentx==parenty:
            return False
        
        
        self.parent[parenty] = parentx
        return True
        

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        ans1 = [-1,-1]
        ans2 = [-1,-1]
        p = {}
        indegree = collections.defaultdict(int)
        for i,edge in enumerate(edges):
            s,d = edge
            indegree[d]+=1
            if indegree[d]==2:
                ans1 = [p[d],d]
                ans2 = [s,d]
                edges[i][1]=0
                break
            
            p[d] = s
            
            
        
        uf = UnionFind()
        
        for s,d in edges:
            if d == 0:
                continue
            if not uf.union(s,d):
                if ans1[0] == -1:
                    return [s,d]
                return ans1
        
        return ans2
        

        