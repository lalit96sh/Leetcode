class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        nums = sorted((q,w,w/q) for q,w  in zip(quality,wage))
        
        from heapq import heappop,heappush
        h = []
        qsum = 0
        ans = float("inf")
        for q,w,r in nums:
            heappush(h,(-r,q))
            qsum+=q
            if len(h)>k:
                rat,quality = heappop(h)
                qsum -= quality
            if len(h)==k:
                ans = min(ans,-h[0][0]*qsum)
        
        return ans