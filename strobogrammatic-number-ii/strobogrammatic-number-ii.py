class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        single = ["0","1","8"]
        mp = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        
        ans = []
        
        def dfs(rem,left,is_first):
            # print(rem)
            if rem==0:
                ans.append(left+"".join([mp[l] for l in left[::-1]]))
                return
            if rem==1:
                for s in single:
                    ans.append(left+s+"".join([mp[l] for l in left[::-1]]))
                return
            
            for key in mp.keys():
                if is_first and key=="0":
                    continue
                dfs(rem-2,left+key,False)
        
        dfs(n,"",True)
        
        
        return ans
                
        