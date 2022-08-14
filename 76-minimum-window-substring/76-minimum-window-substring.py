class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = collections.defaultdict(lambda:0)
        for tt in t:
            t_map[tt]+=1
        count = len(t_map)
        mp = collections.defaultdict(lambda:0)
        ans = float("inf")
        val = ""
        start = 0
        cnt = 0
        for i,st in enumerate(s):
            
            if t_map[st]:
                mp[st]+=1
                if mp[st]==t_map[st]:
                    cnt+=1
            
            while count==cnt:
                if ans>i-start+1:
                    ans = i-start+1
                    val = s[start:i+1]
                    
                
                if t_map[s[start]]:
                    if mp[s[start]]==t_map[s[start]]:
                        cnt-=1
                    mp[s[start]]-=1

                start+=1
                
        
        
        return val
            
            
        
        
        
        
        
        
                
        
                
                
            
                
        