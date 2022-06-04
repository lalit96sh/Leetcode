class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        last_e = intervals[0][1]
        cnt = 0
        for start,end in intervals[1:]:
            if start>=last_e:
                last_e = end
                continue
            cnt+=1
            last_e = min(last_e,end)
        return cnt
            
                
        