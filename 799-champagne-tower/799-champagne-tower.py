class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        # if query_row ==0:
        #     return 1 if poured>=1 else poured
        
        q = collections.deque()
        
        q.append(poured)
        
        level = 0
        flag = False
        while q:
            
            if level==query_row:
                flag = True
            qlen = len(q)
            mp = [0]*(qlen+1)
            for i in range(qlen):
                val = q.popleft()
                excess,val = max(0,val-1), min(val,1)
                
                if flag and query_glass==i:
                    return val
                
                if excess:
                    mp[i]+=excess/2
                    mp[i+1]+=excess/2
            q.extend(mp) 
            level+=1
            
            
        return 0