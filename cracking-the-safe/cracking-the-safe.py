class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        cur = "0"*(n-1)
        vis = set()
        # vis.add(cur)
        
        for i in range(k**n):
            
            last = cur[-(n-1):] if n-1 !=0 else ""
            for j in range(k-1,-1,-1):
                node_st = last+str(j)
                if  node_st not in vis:
                    vis.add(node_st)
                    cur+=str(j)
                    break
        
        return cur
                
        
        