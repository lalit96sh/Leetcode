class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        n = len(start)
        ans = [start[0]]
        i = 1
        j = 0
        while i<n and j<n:
            
            if end[j]>start[i]:
                ans.append(start[i])
                i+=1
            else:
                i+=1
                j+=1
        return len(ans)
                
        