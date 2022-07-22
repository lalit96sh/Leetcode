class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        dis = collections.defaultdict(lambda: float("inf"))
        
        for i in range(n):
            dis[(i,i)] = 0
        
        
        for s,d,w in edges:
            dis[(s,d)] = w
            dis[(d,s)] = w
            
        
        for k in range(n):
            
            for i in range(n):
                for j in range(i+1,n):
                    
                    if dis[(i,j)]>dis[(i,k)]+dis[(k,j)]:
                        dis[(i,j)]= dis[(j,i)] = dis[(i,k)]+dis[(k,j)]
                        
                        
        ans = -1
        mn = float("inf")
        # print(dis)
        # for i in range(n):
        #     print([dis[(i,j)] for j in range(n)])
        for i in range(n):
            count = 0
            for j in range(n):
                if dis[(i,j)]<=distanceThreshold:
                    count+=1
            
            if count<=mn:
                mn = count
                ans = i
                
        return ans
                
                
                
        
        