class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid),len(grid[0])
        
        def dfs():
            
            q = [(-grid[0][0],0,0)]
            import heapq
            seen = set()
            seen.add((0,0))

            while q:
                val,i,j = heapq.heappop(q)

                if i==m-1 and j==n-1:
                    return -val
                

                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:

                    x,y = i+di, j+dj

                    if 0<=x<m and 0<=y<n and (x,y) not in seen:
                        seen.add((x,y))
                        heapq.heappush(q,(max(val,-grid[x][y]),x,y))

            
                        
                
            
        
        y = dfs()
        # print(memo)
        return y
            
            
            
            
            