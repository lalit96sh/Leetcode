class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        move = {(1,0): "r",(0,1): "u",(-1,0):"l",(0,-1): "d"}

        def dfs(i,j):
            grid[i][j] = 0
            
            ans = []

            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+di,j+dj

                if (not (0<=x<m and 0<=y<n)) or grid[x][y]==0:
                    continue

                ans.append(move[(di,dj)])

                ans.append(dfs(x,y))
            
            return tuple(ans)
        mp = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mp.add(dfs(i,j))
        return len(mp)
                        
                
        
        
                
                
                
        