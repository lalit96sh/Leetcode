class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tmap = collections.defaultdict(int)
        
        for tt in t:
            tmap[tt]+=1
        
        keycnt = len(tmap)
        
        
        mp = collections.defaultdict(int)
        cnt=0
        start = 0
        anslen = float("inf")
        ans = ""
        for i,ss in enumerate(s):
            
            if tmap[ss]:
                mp[ss]+=1
                if tmap[ss]==mp[ss]:
                    cnt+=1
            # print(start,i,cnt,mp)
            if cnt==keycnt:
                
                while cnt==keycnt:
                    if tmap[s[start]]:
                        if tmap[s[start]]==mp[s[start]]:
                            cnt-=1
                        mp[s[start]]-=1
                    
                    if anslen>i-start+1:
                        anslen = i-start+1
                        ans = s[start:i+1]
                    start+=1
        return ans
            
            
        
        
        
        
        
        
                
        
                
                
            
                
        