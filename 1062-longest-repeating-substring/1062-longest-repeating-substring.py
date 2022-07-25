class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        n = len(s)
        for l in range(n-1,0,-1):
            mp = set()
            for i in range(n-l+1):
                if s[i:i+l] in mp:
                    return l
                mp.add(s[i:i+l])
        
        return 0
                
                
                
        