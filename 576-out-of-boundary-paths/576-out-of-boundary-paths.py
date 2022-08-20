class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        memo = {}
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(x,y,k):
            if not(0<=x<m and 0<=y<n):
                return 1
            if k==0:
                return 0
            
            if (x,y,k) not in memo:
                count = 0
                for dx,dy in drs:
                    i,j = x+dx,y+dy
                    count+=dfs(i,j,k-1)
            
            
                memo[(x,y,k)] = count        
                
                
                
            return memo[(x,y,k)]
        
        return dfs(startRow,startColumn,maxMove)%((10**9)+7)