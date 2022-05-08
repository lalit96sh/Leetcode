class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            
            if height[l] < height[r]:
                h = height[l]
                l+=1
            else:
                h = height[r]
                r-=1
            
            w = r-l+1
            ans = max(ans,h*w)
        return ans
            
        