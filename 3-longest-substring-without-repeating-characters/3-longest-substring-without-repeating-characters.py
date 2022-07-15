class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        mp = {}
        start = 0
        ans = 1
        for i,st in enumerate(s):
            if st in mp:
                ans = max(ans,i-start)
                start=max(start,mp[st]+1)
            
            mp[st]=i
        return max(ans,len(s)-start)
            
        