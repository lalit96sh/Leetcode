class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        counter = Counter(nums)
        ans = []
        n = len(nums)
        def dfs(cur):
            
            if len(cur)==n:
                ans.append(cur[:])
                return
            
            for key in counter:
                if counter[key]:
                    counter[key]-=1
                    cur.append(key)
                    dfs(cur)
                    cur.pop()
                    counter[key]+=1
        dfs([])
        return ans