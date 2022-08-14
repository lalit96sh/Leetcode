class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        r = 0
        j = 0
        for i in range(len(intervals)):
            if start[i]>=end[j]:
                r-=1
                j+=1
            r+=1
    
        return r
                