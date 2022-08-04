class Solution:
    def maxA(self, n: int) -> int:
        
        memo = {}
        def dfs(start,increment,val):
            if start==n:
                return val
            if start>=n+1:
                return val-increment
            if (start,increment,val) not in memo:
                as_usual_incremet = dfs(start+1, increment, val + increment)

                copy_paste = dfs(start+3,val,2*val)

                memo[(start,increment,val)] = max(as_usual_incremet,copy_paste)
            return memo[(start,increment,val)]
        
        return dfs(0,1,0)
                
            
            
            