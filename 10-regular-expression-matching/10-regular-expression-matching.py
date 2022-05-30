class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        
        dp = [[False]*(np+1)for _ in range(ns+1)]
        
        dp[0][0] = True
        
        for i in range(ns+1):
            for j in range(1,np+1):
                if i==0:
                    if p[j-1]=="*":
                        dp[i][j]=dp[i][j-2]
                    continue

                if p[j-1]==s[i-1] or p[j-1]==".":
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":
                    dp[i][j]=dp[i][j-2] # zero occurence
                    if ((p[j-2]==s[i-1]) or (p[j-2]==".")):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        # print(dp)
        for i in range(ns+1):
            print(dp[i])
        return dp[ns][np]
                