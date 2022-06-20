class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        def f(st):
            ans = []
            mp = {}
            for i in range(n):
                if st[i] not in mp:
                    mp[st[i]] = i
                ans.append(str(mp[st[i]]))
            return " ".join(ans)
        a = f(s)
        b = f(t)
        print(a)
        print(b)
        return a==b
        