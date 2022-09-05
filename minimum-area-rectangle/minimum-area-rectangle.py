# class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
        
#         pts = set([(x,y) for x,y in points])
        
#         n = len(points)
#         mn = float("inf")
#         for i in range(n):
#             for j in range(i+1,n):

#                 if points[i][0]==points[j][0] or points[i][1]==points[j][1]:
#                     continue
                
#                 if (points[i][0],points[j][1]) in pts and (points[j][0],points[i][1]) in pts:
                    
#                     mn = min(mn,abs(points[i][1]-points[j][1])*abs(points[i][0]-points[j][0]))
                    
#         return mn if mn!=float("inf") else 0
    
# class Solution(object):
#     def minAreaRect(self, points):
#         S = set(map(tuple, points))
#         ans = float('inf')
#         for j, p2 in enumerate(points):
#             for i in range(j):
#                 p1 = points[i]
#                 if (p1[0] != p2[0] and p1[1] != p2[1] and
#                         (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
#                     ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
#         return ans if ans < float('inf') else 0    
class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
        
            
            
        
        
        
        