class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = [i for i in coins if i<=amount]
        if amount==0:
            return 0
        
        q = collections.deque()
        vis = set()
        for coin in coins:
            
            if coin==amount:
                return 1
            if coin not in vis and coin<amount:
                vis.add(coin)
                q.append(coin)
            
        level=1
        while q:
            level+=1
            qlen = len(q)
            
            for _ in range(qlen):
                
                cur_sum = q.popleft()
                
                for coin in coins:
                    if (cur_sum+coin)==amount:
                        return level
                    if cur_sum+coin not in vis and (cur_sum+coin)<amount:
                        q.append(cur_sum+coin)
                        vis.add(cur_sum+coin)
        return -1
            
        
                    
                    
                
                
        