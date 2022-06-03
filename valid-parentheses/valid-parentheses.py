class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            "(": 1,
            ")":-1,
            "[": 2,
            "]":-2,
            "{": 3,
            "}":-3,
        }
        
        st = []
        
        for ss in s:
            if mp[ss]<0:
                if not st or st[-1]+mp[ss]!=0:
                    return False
                st.pop()
            else:
                st.append(mp[ss])
        
        return False if st else True
        
        
        
        