class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        if not blocked:
            return True
        n = 1e6
        blocked = set([(i,j) for i,j in blocked])
        area = 200*199/2
        
        def bfs(source,target):
            seen = set()
            q = [(source[0],source[1])]
            seen.add((source[0],source[1]))
            blocks = 1
            while q:
                i,j = q.pop()
                if i == target[0] and j == target[1]:
                    return True
                if blocks>area:
                    return True
                for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x = i+di
                    y = j+dj

                    if 0<=x<n and 0<=y<n and (x,y) not in blocked and (x,y) not in seen:
                        blocks+=1
                        seen.add((x,y))
                        q.append((x,y))
            return False
        
        return bfs(source,target) and bfs(target,source)
        