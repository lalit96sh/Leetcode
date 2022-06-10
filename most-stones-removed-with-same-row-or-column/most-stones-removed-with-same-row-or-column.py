class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        mpc = collections.defaultdict(set)
        mpr = collections.defaultdict(set)
        
        mp = collections.defaultdict(set)
        
        for x,y in stones:
            cur_point = (x,y)
            for parent in [mpr[x],mpc[y]]:
                for point in parent:
                    mp[point].add(cur_point)
                    mp[cur_point].add(point)
            
            mpr[x].add(cur_point)
            mpc[y].add(cur_point)
        print(mpr)
        print(mpc)
        print(mp)
            
        vis = set()
        def dfs(p):
            vis.add(p)
            
            for neigh in mp[p]:
                if neigh not in vis:
                    dfs(neigh)
            
        cnt = 0
        for p in stones:
            p = tuple(p)
            if p not in vis:
                cnt+=1
                dfs(p)
        
        return len(stones)-cnt
                
                
                
                
        