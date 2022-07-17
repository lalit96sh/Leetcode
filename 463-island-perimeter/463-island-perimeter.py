class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        def dfs(i,j):
            grid[i][j]=-1
            
            ans = 0
            
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+di,j+dj
                
                if (not (0<=x<r and 0<=y<c)) or grid[x][y]==0:
                    ans+=1
                    continue
                if grid[x][y]==1:
                    ans+=dfs(x,y)
            
            return ans
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return dfs(i,j)
            
            
            
        