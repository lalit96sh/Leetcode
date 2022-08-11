class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        nm = [(m,i) for i,m  in enumerate(nums)]
        
        nm.sort()
        mn = float("inf")
        ans = 0
        for val,index in nm:
            if mn>index:
                mn = index
            else:
                ans = max(index-mn,ans)
                
        return ans
                