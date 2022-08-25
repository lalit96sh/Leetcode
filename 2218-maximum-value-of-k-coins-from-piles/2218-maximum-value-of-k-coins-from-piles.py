class Solution:
    def maxValueOfCoins(self, A: List[List[int]], k: int) -> int:
        
#         n = len(piles)
#         memo = {}
#         def dfs(start,k):
            
#             if k==0 or start==n:
#                 return 0
            
#             if (start,k) not in memo:
            
#                 res = dfs(start+1,k)
#                 sm = 0
                
#                 for i in range(min(len(piles[start]),k)):
#                     sm += piles[start][i]
#                     res = max(res,sm+dfs(start+1,k-1-i))

                    
                
                
#                 memo[(start,k)] = res
            
#             return memo[(start,k)]
#         return dfs(0,k)
        @functools.lru_cache(None)
        def dp(i, k):
            if k == 0 or i == len(A): return 0
            res, cur = dp(i + 1, k), 0
            for j in range(min(len(A[i]), k)):
                cur += A[i][j]
                res = max(res, cur + dp(i+1, k-j-1))
            return res
        
        return dp(0, k)
            
        