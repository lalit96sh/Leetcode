class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        mx_row = [max(g) for g in grid]
        
        mx_col = [max([grid[j][i] for j in range(n)])  for i in range(n)]
        
        ans = 0
        for i in range(n):
            for j in range(n):
                
                ans += min(mx_row[i],mx_col[j]) - grid[i][j]
        
        return ans