class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        n = len(s)
        mp  = collections.defaultdict(lambda:0)
        dp = [0]*(n+1)
        
        
        for i in range(n):
            
            cur = dp[i]+1-mp[s[i]]
            mp[s[i]]=dp[i]+1
            
            dp[i+1] = dp[i]+cur
            
        return dp[n]%(10**9+7)
            