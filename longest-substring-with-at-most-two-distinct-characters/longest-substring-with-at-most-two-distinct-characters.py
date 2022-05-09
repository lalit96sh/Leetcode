class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        n = len(s)
        
        if n<=2:
            return n
        
        mp = collections.defaultdict(int)
        cnt = 0
        start = 0
        ans = 0
        for i,ss in enumerate(s):
            
            if not mp.get(ss):
                cnt+=1
            
            mp[ss]+=1
            
            while cnt>2:
                mp[s[start]]-=1
                if not mp[s[start]]:
                    cnt-=1
                start+=1
            
            ans = max(ans,i-start+1)
        return ans
        