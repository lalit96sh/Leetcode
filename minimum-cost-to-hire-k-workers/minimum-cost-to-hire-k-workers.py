class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        qwr = sorted((w/q,q,w) for q,w  in zip(quality,wage))
        
        
        quality_sum = 0
        from heapq import heappush,heappop
        h = []
        ans = float("inf")
        
        for r,q,w in qwr:
            
            heappush(h,-q)
            quality_sum+=q
            
            if len(h)>k:
                quality_sum+=heappop(h)
            
            if len(h)==k:
                ans = min(ans,r*quality_sum)
        return ans