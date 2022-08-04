class Solution:
    def longestRepeatingSubstring(self, st: str) -> int:
        n = len(st)
        
        
        def is_present(l):
            mp = set()
            for i in range(n-l+1):
                if st[i:i+l] in mp:
                    return True
                mp.add(st[i:i+l])
            return False
        
        
        s = 0
        e = n-1
        
        while s<e:
            l = (s+e+1)//2
            if is_present(l):
                s = l
            else:
                e=l-1
        
        return s
                
                
                
        