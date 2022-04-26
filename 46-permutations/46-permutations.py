class Solution:
    def permute(self, cur: List[int]) -> List[List[int]]:
        
        n = len(cur)
        ans = []
        
        def f(start):
            if start==n:
                ans.append(cur[:])
                
            for i in range(start,n):
                cur[i],cur[start] = cur[start],cur[i]
                f(start+1)
                cur[i],cur[start] = cur[start],cur[i]
        
        f(0)
        return ans
                
                