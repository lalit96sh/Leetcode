class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def f(i,j):
            if not (0<=i<m and 0<=j<n):
                return
            if grid[i][j]=="0":
                return
            
            grid[i][j]="0"
            
            for r,c in [(0,1),(0,-1),(1,0),(-1,0)]:
                f(r+i,j+c)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    f(i,j)
        return count