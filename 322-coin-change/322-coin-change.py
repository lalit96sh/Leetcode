class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # coins = 0
        if amount==0:
            return 0
        
        q = [_ for _ in coins if _ <= amount]
        
        curq = [(v,1) for v in q]
        vis = set()
        
        while curq:
            
            val,cs = curq.pop(0)
            
            if val == amount:
                return cs
            
            for _ in q:
                if _+val<=amount and _+val not in vis:
                    curq.append((_+val,cs+1))
                    vis.add(_+val)
            
            
        return -1
        
                    
                    
                
                
        