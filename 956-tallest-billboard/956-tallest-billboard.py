class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        """
        
        dp = 
        
        {
            0:
            1:
            2:
            3:
            4:
        }
        
        max(4+3)
        
        """
        
        
        
        dp = {}
        dp[0] = 0
        
        for x in rods:
            temp = copy.deepcopy(dp)
            for d in temp:
                dp[d+x] = max(temp[d],dp.get(d+x,0))
                
                dp[abs(d-x)] = max(dp.get(abs(d-x),0), temp[d]+min(d,x))

        
        return dp[0]
        
        
        