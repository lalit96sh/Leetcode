class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        memo = {}
        def dfs(start,end):
            
            if start==end:
                return 0
            if start>end:
                -start
            if (start,end) in memo:
                return memo[(start,end)]
            mx = float("inf")
            for i in range(start,end+1):
                mx = min(i+max(dfs(start,i-1),dfs(i+1,end)), mx)
                
            memo[(start,end)] = mx if mx != float("inf") else 0
            return memo[(start,end)]
        
        return dfs(1,n)