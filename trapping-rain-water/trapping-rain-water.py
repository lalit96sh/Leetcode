class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        l = 0
        r = n-1
        
        leftmax = rightmax = 0
        ans = 0
        
        while l<r:
            
            if height[l]<height[r]:
                
                if height[l]<=leftmax:
                    ans += (leftmax-height[l])
                else:
                    leftmax = height[l]
                l+=1
            else:
                
                if rightmax>=height[r]:
                    ans+=(rightmax-height[r])
                else:
                    rightmax = height[r]
                r-=1
        return ans
        