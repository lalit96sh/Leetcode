class unionfind:
    def __init__(self,m,n):
        self.rows = m
        self.cols = n
        self.pos = collections.defaultdict(int)
        self.parent = {(i,j):(i,j) for j in range(n) for i in range(m)}
        self.rank = collections.defaultdict(int)
        self.islands = 0
    
    def find(self,node):
        
        while self.parent[node]!=node:
            node = self.parent[node]
        
        return node
    
    def add_island(self,node):
        if self.pos[node]==1:
            return
        x,y = node
        self.islands+=1
        self.pos[node] = 1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            xx,yy = x+dx,y+dy
            if not(0<=xx<self.rows and 0<=yy<self.cols) or self.pos[(xx,yy)]==0:
                continue
            find = self.find((xx,yy))
            self.union(node,find)
    
    def union(self,rx,ry):
        x = self.find(rx)
        y = ry #self.find(y)
        
        if x!=y:
            if self.rank[x]>self.rank[y]:
                self.parent[y] = x
            elif self.rank[x]<self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x]+=1
            self.islands-=1
                

    def get_islands(self):
        return self.islands

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        uf = unionfind(m,n)
        ans = []
        for node in positions:
            uf.add_island(tuple(node))
            ans.append(uf.get_islands())
        return ans
        
        
        
        