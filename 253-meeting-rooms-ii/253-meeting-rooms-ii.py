class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        h = []
        intervals.sort()
        
        from heapq import heappush,heappop
        
        heappush(h,intervals[0][1])
        
        for s,e in intervals[1:]:
            
            if h[0]<=s:
                heappop(h)
                
            heappush(h,e)
            
        return len(h)
                