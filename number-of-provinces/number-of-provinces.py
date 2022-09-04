
class UnionFind:
    def __init__(self,size):
        self.rank = [1]*size
        self.root = [i for i in range(size)]
        self.count = size
        
    def get_count(self):
        return self.count
    
    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.root[rootx]=rooty
            else:
                self.root[rooty]=rootx
                self.rank[rootx]+=1
            self.count-=1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        # def dfs(node):
        #     isConnected[node][node]=0
        #     for i in range(n):
        #         if i!=node and isConnected[node][i]==1:
        #             isConnected[node][i]=0
        #             isConnected[i][node]=0
        #             dfs(i)
        # level = 0
        # for i in range(n):
        #     if isConnected[i][i]==1:
        #         level+=1
        #         dfs(i)
        # return level
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    uf.union(i,j)
        return uf.get_count()

                    
            
            
        