class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
#         if len(p)>len(s):
#             return []
        
#         result = []
        
#         freq = collections.defaultdict(int)
        
#         def update_freq(c,step):
#             freq[c]+=step
#             if not freq[c]:
#                 del freq[c]
                
#         n = len(p)
            
#         for i in p:
#             update_freq(i,-1)

#         for i in range(len(s)):
#             if not freq:
#                 result.append(i-n)
#             if i>=n:
#                 update_freq(s[i-n],-1)
#             update_freq(s[i],1)
            
            
#         if not freq:
#             result.append(len(s)-n)
#         return result
        
        def order(st):
            return ord(st)-ord("a")
        p_mp  = [0]*26
    
        for pp in p:
            p_mp[order(pp)]+=1
            
        
        n = len(p)
        mp = [0]*26
        ans = []
        for i,st in enumerate(s):
            
            mp[order(st)]+=1
            
            if i>=n:
                mp[order(s[i-n])]-=1
            
            if mp==p_mp:
                ans.append(i-n+1)
        return ans
            
        
        
        