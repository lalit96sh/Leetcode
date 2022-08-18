class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(s_start,p_start):
            if (s_start,p_start) not in memo:
                if p_start==len(p):
                    ans = (s_start==len(s))
                else:
                    letter_match = s_start<len(s) and p[p_start] in [".", s[s_start]]
                    
                    if p_start+1<len(p) and p[p_start+1]=="*":
                        ans = dp(s_start, p_start+2) or (letter_match and dp(s_start+1,p_start))
                    else:
                        ans = letter_match and dp(s_start+1,p_start+1)
                
                
                memo[(s_start,p_start)] = ans
            return memo[(s_start,p_start)]
        return dp(0,0)
                    
                