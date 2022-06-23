class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        w = set(wordDict)
        n = len(s)
        dp = {}
        def f(start):
            if start in dp:
                return dp[start]
            if start==n:
                return True
            for i in range(start,n):
                if s[start:i+1] in w:
                    if f(i+1):
                        return True
            dp[start] = False
            return False
        return f(0)
        