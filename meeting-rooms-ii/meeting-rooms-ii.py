class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        r = 1
        ans = 1
        i=1
        j = 0
        n = len(start)
        while i < n and j<n:
            
            if end[j]<=start[i]:
                r-=1
                j+=1
            else:
                i+=1
                r+=1
            ans=max(ans,r)
        return ans
                