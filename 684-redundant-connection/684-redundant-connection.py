class UnionFind:
    
    def __init__(self):
        self.rank = collections.defaultdict(int)
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
        
        if self.rank[parentx] < self.rank[parenty]:
            self.parent[parentx] = parenty
        elif self.rank[parenty] < self.rank[parentx]:
            self.parent[parenty] = parentx
        else:
            self.parent[parenty] = parentx
            self.rank[parentx]+=1
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind()
        
        for s,d in edges:
            if not uf.union(s,d):
                return [s,d]
        
        return []
        
        
        