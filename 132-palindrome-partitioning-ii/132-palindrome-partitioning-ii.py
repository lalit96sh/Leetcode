class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        mp = {
            i:i
            for i in range(-1,n)
        }
        # mp[-1] = -1
        
        for i in range(n):
            mp[i] = min(mp[i],1+mp[i-1])
            
            for j,k in [[i,i+1],[i-1,i+1]]:
                
                while j>=0 and k<n and s[j]==s[k]:
                    mp[k] = min(mp[j-1]+1,mp[k])
                    j-=1
                    k+=1
        return mp[k-1]            
        
        