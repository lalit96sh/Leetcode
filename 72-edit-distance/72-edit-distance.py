class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        n1,n2 = len(w1),len(w2)
        memo = {}
        def dfs(s1,s2):
            
            if s1==n1:
                return n2-s2
            elif s2==n2:
                return n1-s1
            
            if (s1,s2) not in memo:
                
                if w1[s1]==w2[s2]:
                    memo[(s1,s2)] = dfs(s1+1,s2+1)
                    
                else:
                    memo[(s1,s2)] = 1 + min(dfs(s1+1,s2),dfs(s1,s2+1),dfs(s1+1,s2+1))
                
            return memo[(s1,s2)]
        
        return dfs(0,0)