class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        ns = len(s)
        nt = len(t)
        i,j = ns-1,nt-1
        skip_s,skip_t = 0,0
        while i>=0 and j>=0:
            if s[i]=="#":
                skip_s+=1
                i-=1
                continue
            if t[j]=="#":
                skip_t+=1
                j-=1
                continue
                
            if skip_s or skip_t:
                if skip_s:
                    skip_s-=1
                    i-=1
                if skip_t:
                    skip_t-=1
                    j-=1
                continue
            
            print(i,j,skip_s,skip_t)
            if s[i]!=t[j]:
                return False
            i-=1
            j-=1
        while i>=0 and (s[i]=="#" or skip_s>0):
            if s[i]=="#":
                skip_s+=1
            else:
                skip_s-=1
            i-=1
        while j>=0 and (t[j]=="#" or skip_t>0):
            skip_t+= (1 if t[j]=="#" else -1)
            j-=1
        return i<0 and j<0
            
        