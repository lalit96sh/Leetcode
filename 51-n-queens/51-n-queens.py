class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        queens = [["."]*n for _ in range(n)]
        
        ans = []
        def is_present(x,y):
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i==0 and j==0:
                        continue
                    for k in range(1,n):
                        px,py = x + (k*i), y + (k*j)
                        
                        if not (0<=px<n and 0<=py<n):
                            break
                        
                        if queens[px][py]=="Q":
                            return True
            return False
        
        def func(queens):
            return ["".join(row) for row in queens]
        
        def dfs(i):
            
            if i==n:
                return ans.append(func(queens[:]))
            
            
            # for i in range(i,n):
            for j in range(n):

                if is_present(i,j):
                    continue

                queens[i][j] = "Q"

                dfs(i+1)

                queens[i][j] = "."
                    
            return False
        for j in range(n):
            queens[0][j] = "Q"
            dfs(1)

            queens[0][j] = "."
        return ans
                
            
        