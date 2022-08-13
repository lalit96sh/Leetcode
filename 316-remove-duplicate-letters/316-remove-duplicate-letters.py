class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        def recurse(s):
            if not s:
                return ""
            
            c = Counter(s)
            
            mn = 0
            
            
            for i,st in enumerate(s):
                
                if st<s[mn]:
                    mn = i
                    
                c[st]-=1
                
                if c[st]==0:
                    break
                    
            return s[mn]+recurse(s[mn+1:].replace(s[mn],""))
        return recurse(s)
            