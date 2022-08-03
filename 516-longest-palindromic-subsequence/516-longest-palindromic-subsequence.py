class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = {}
        def dfs(start,end):
            
            if start>end:
                return 0
            
            if start==end:
                return 1
            
            if (start,end) not in memo:
                
                if s[start]==s[end]:
                    memo[(start,end)] = 2+dfs(start+1,end-1)
                
                else:
                    memo[(start,end)] = max(dfs(start+1,end),dfs(start,end-1))
                
                
            return memo[(start,end)]
        
        return dfs(0,len(s)-1)
        