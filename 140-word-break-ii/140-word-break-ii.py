class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        w = set(wordDict)
        n = len(s)
        dp = {}
        r = []
        def f(start,cur):
            if start==n:
                r.append(cur.strip())
                return
            for i in range(start,n):
                if s[start:i+1] in w:
                    f(i+1," ".join([cur,s[start:i+1]]))
        f(0,"")
        return r