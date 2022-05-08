class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start = 0
        mp = {}
        cnt = 0
        ans = 0
        n = len(fruits)
        
        for i,fr in enumerate(fruits):
            if fr not in mp or mp.get(fr)==0:
                cnt+=1
                mp[fr] = 0
            # print(i,start)
            mp[fr]+=1
            # print(mp)
            while cnt>2:
                
                # print(mp[fruits[start]])
                mp[fruits[start]]-=1
                if mp[fruits[start]] == 0:
                    cnt-=1
                start+=1
            ans = max(ans,i-start+1)
            
            
        return max(ans,n-start)