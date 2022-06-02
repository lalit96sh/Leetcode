class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        n = len(s)
        ns = len(sources)
        
        mp = {}
        
        for i,ind in enumerate(indices):
            mp[ind] = (sources[i],targets[i])
        
        # print(mp)
        i,j,ans = 0,0,""
        while i < n:
            # print(i in mp,i,mp)
            if i in mp:
                ln = len(mp[i][0])
                
                if s[i:i+ln]==mp[i][0]:
                    # print("gotchaaa")
                    ans+=mp[i][1]
                    i+=ln
                    continue
            #     print("got but not poss")
            # print("norma")  
            ans+=s[i]
            i+=1
        return ans