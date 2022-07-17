class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        '''
        2,10 highest height
        
        9,0 highest height
        
        
        
        '''
        
        buildings = sorted([(x1,-h,x2) for x1,x2,h in buildings] + [(x2,0,None) for x1,x2,h in buildings])
        
        
        H = [(0,float("inf"))] # height,till position height is valid
        ans = [(0,0)]
        from heapq import heappush, heappop
        
        for x1,h,x2 in buildings:
            
            while H[0][1]<=x1:
                heappop(H)
            
            if x2:
                heappush(H,(h,x2))
                
            if ans[-1][1]!=-H[0][0]:
                ans.append([x1,-H[0][0]])
                
        return ans[1:]