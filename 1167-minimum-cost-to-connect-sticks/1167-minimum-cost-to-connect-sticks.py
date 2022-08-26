class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        h = []
        from heapq import heappop,heappush
        for st in sticks:
            heappush(h,st)
        ans = 0
        while len(h)>1:
            f,s = heappop(h),heappop(h)
            ans+=(f+s)
            heappush(h,f+s)
            
       
        
        return ans
            
            

        