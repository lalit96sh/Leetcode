class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        ans = 1
        
        points.sort()
        last_e = points[0][1]
        # print(points)
        for start,end in points[1:]:
            # print(start,last_e)
            if start>last_e:
                ans+=1
                last_e = end
                continue
            
            last_e = min(last_e,end)
        
        return ans
                