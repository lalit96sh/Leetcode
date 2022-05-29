class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        k = len(costs[0])
        
        if n == 0:
            return 0
        
        
        
            
        prev_max , prev_max_index, prev_max_second = None,None,None
        for color in range(k):
            if prev_max is None or  costs[0][color]<prev_max:
                prev_max_index = color
                prev_max_second = prev_max
                prev_max=costs[0][color]
            elif prev_max_second is None or costs[0][color]<prev_max_second:
                prev_max_second = costs[0][color]
                
        for i in range(1,n):
            cur_max, cur_max_second, cur_max_index = None,None,None
            for j in range(k):
                costs[i][j]+=(prev_max if j!=prev_max_index else prev_max_second)
                if cur_max is None or  costs[i][j]<cur_max:
                    cur_max_index = j
                    cur_max_second = cur_max
                    cur_max=costs[i][j]
                elif cur_max_second is None or costs[i][j]<cur_max_second:
                    cur_max_second = costs[i][j]
            
            prev_max_index = cur_max_index
            prev_max_second = cur_max_second
            prev_max=cur_max
        
        return prev_max
                
        
                