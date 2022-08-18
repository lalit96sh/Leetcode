class Solution:
    def numSquares(self, n: int) -> int:
        
        sq = [i*i for i in range(1,int(n**0.5)+1)]
        
        q = collections.deque([n])
        
        level = 0
        while q:
            qlen = len(q)
            
            for _ in range(qlen):
                ele = q.popleft()
                
                for s in sq:
                    if s==ele:
                        return 1+level
                    elif s>ele:
                        break
                    else:
                        q.append(ele-s)
            level+=1
        return level
                