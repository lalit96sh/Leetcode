class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        
        mp = collections.defaultdict(list)
        for i,x in enumerate(arr):
            mp[x].append(i)
        
        q = [0]
        jump = 0
        v = [False]*n
        v[0]=True
        while q:
            qlen = len(q)
            for _ in range(qlen):
                i = q.pop(0)
                if i==n-1:
                    return jump
                ids = mp[arr[i]]
                ids.append(i+1)
                ids.append(i-1)
                    
                for j in ids:
                    if 0<=j<n and (not v[j]):
                        v[j] = True
                        q.append(j)
                del mp[arr[i]]
            jump+=1