class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
   
        n = len(stones)
    
        if (n-1)%(k-1):
            return -1
        
        prefix = {-1:0}
        
        for i,st in enumerate(stones):
            prefix[i] = prefix[i-1]+st
        
        
        memo = {}
        def dfs(start,end):
            if end-start+1<k:
                return 0
            
            if (start,end) not in memo:
                res = min([
                    dfs(start,i)+dfs(i+1,end) for i in range(start,end,k-1)
                ])

                if (end-start)%(k-1)==0:
                    res+=prefix[end]-prefix[start-1]
                memo[(start,end)] = res
            return memo[(start,end)]
        return dfs(0,n-1)