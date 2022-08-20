class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        def is_perfect(x):
            root = x**0.5
            return (int(root))**2==x
        
        mp = collections.defaultdict(list)
        n = len(nums)
        counter = collections.Counter(nums)
        
        for i in counter:
            
            for j in counter:
                if is_perfect(i+j):
                    mp[i].append(j)
                    
        
        # print(mp)
        def dfs(num,length):
            
            counter[num]-=1
            
            count = 0
            if length==n-1:
                count=1
            else:
                for nm in mp[num]:
                    if counter[nm]:
                        count+=dfs(nm,length+1)

            
            counter[num]+=1

            return count
        ans = 0
        for v in counter:
            ans+=dfs(v,0)
            
        return ans
            
                    
                    
        