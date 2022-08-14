class Solution:
    def canReach(self, a: List[int], start: int) -> bool:
        
        n = len(a)
        
        q = []
        
        q.append(start)
        v = set()
        v.add(start)
        while q:
            i = q.pop()
            num = a[i]
            if num==0:
                return True
            if 0<=i+num<n and i+num not in v:
                q.append(i+num)
                v.add(i+num)
            if 0<=i-num<n and i-num not in v:
                q.append(i-num)
                v.add(i-num)
                
        return False
        