class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        if str1==str2:
            return True
        mp = {}
        seen = set()
        for i,st in enumerate(str1):
            if st in mp and mp[st]!=str2[i]:
                return False

            mp[st]=str2[i]
            seen.add(str2[i])
            
        
        return len(seen)<26
            
        