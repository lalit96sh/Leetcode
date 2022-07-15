class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1)
        n2 = len(text2)
        
        memo = {}
        
        def dfs(s1,s2):
            if s1==n1 or s2 == n2:
                return 0
            
            if (s1,s2) in memo:
                return memo[(s1,s2)]
            
            if text1[s1]==text2[s2]:
                memo[(s1,s2)] = 1 + dfs(s1+1,s2+1)
            else:
                memo[(s1,s2)] = max(dfs(s1+1,s2),dfs(s1,s2+1))
            return memo[(s1,s2)]
        
        return dfs(0,0)