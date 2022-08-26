class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dfs(start,end):
            
            if end-start<2:
                return 0
            
            ans = float("inf")
            
            for i in range(start+1,end):
                
                ans = min(ans,values[start]*values[i]*values[end] + dfs(start,i) +  dfs(i,end) )
                
            return ans
        
        return dfs(0,len(values)-1)
            
            
        