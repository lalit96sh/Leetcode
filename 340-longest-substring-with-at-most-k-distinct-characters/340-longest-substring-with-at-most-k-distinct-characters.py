class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s)==0:
            return 0
        l = float("-inf")
        n = len(s)
        start = 0
        cnt = 0
        mp = collections.defaultdict(int)
        for i,st in enumerate(s):
            if not mp.get(st):
                cnt+=1
            mp[st]+=1
            
            while cnt>k:
                mp[s[start]]-=1
                if not mp[s[start]]:
                    # del mp[s[start]]
                    cnt-=1
                start+=1
            l = max(l,i-start+1)
        
        return max(l,n-start)
        