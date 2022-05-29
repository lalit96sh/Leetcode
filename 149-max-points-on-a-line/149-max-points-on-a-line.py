class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        r = 1
        for i in range(n-1):
            mp = {}
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                
                if x2-x1==0:
                    mp["inf"]=mp.get("inf",1)+1
                else:
                    slope = ((1.0)*(y2-y1))/(x2-x1)
                    mp[slope]=mp.get(slope,1)+1
            
            r = max(r,max(mp.values()))
        return r
        