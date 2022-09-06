class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1]*n
        
        arr.sort()
        index = {a:i for i,a in enumerate(arr)}
        
        for i in range(1,n):
            root = arr[i]
            
            for j in range(i):
                left = arr[j]
                if root%left==0:
                    right = root//left
                    if right in index:
                        dp[i] += dp[j]*dp[index[right]]
                        dp[i]%=(10**9+7)
        return sum(dp)%(10**9+7)        