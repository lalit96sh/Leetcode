class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.replace("-","")
        
        res = []
        
        n = len(s)
        
        start = n%k
        
        if start:
            res.append(s[:start].upper())
            
        while start<n:
            res.append(s[start:start+k].upper())
            start+=k
        
        return "-".join(res)