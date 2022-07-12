class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j):
            if not (0<=i<m and 0<=j<n):
                return 0
            if grid[i][j]==0:
                return 0
            
            grid[i][j] = 0
            ans = 1
            
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                ans += dfs(i+dx,j+dy)
                
            
            return ans
                
        result = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    result = max(result,dfs(i,j))
                    
        return result