class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def remove_duplicate_stars(p: str):
            new_string = []
            for char in p:
                if not new_string or char != '*':
                    new_string.append(char)
                elif new_string[-1] != '*':
                    new_string.append(char)
            return ''.join(new_string)
        p = remove_duplicate_stars(p)
        ns,np = len(s),len(p)
        memo = {}
        @lru_cache(None)
        def dfs(start_p,start_s):
            if (start_p,start_s) not in memo:
                out_p = start_p==np
                out_s = start_s==ns

                if start_p==np-1 and p[start_p]=="*":
                    res = True
                elif out_p and out_s:
                    res = True

                elif out_p or out_s:
                    res = False

                elif s[start_s]==p[start_p] or p[start_p]=="?":
                    res = dfs(start_p+1,start_s+1)

                elif p[start_p]=="*":
                    res = dfs(start_p+1,start_s) or dfs(start_p,start_s+1)
                else:
                    res = False

                memo[(start_p,start_s)] = res
            
            return memo[(start_p,start_s)]
        return dfs(0,0)
            
            
            
            
            