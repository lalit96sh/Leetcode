class Solution:
    def trap(self, height: List[int]) -> int:
        
#         n = len(height)
#         l = 0
#         r = n-1
        
#         leftmax = rightmax = 0
#         ans = 0
        
#         while l<r:
            
#             if height[l]<height[r]:
                
#                 if height[l]<=leftmax:
#                     ans += (leftmax-height[l])
#                 else:
#                     leftmax = height[l]
#                 l+=1
#             else:
                
#                 if rightmax>=height[r]:
#                     ans+=(rightmax-height[r])
#                 else:
#                     rightmax = height[r]
#                 r-=1
#         return ans
        st = []
        ans = 0
        for i,h in enumerate(height):
            while st and height[st[-1]]<h:
                cur = st.pop()
                if not st:
                    break
                prev = st[-1]
                
                length = i-prev-1
                
                height_diff = abs(height[cur]-min(h,height[prev]))
                
                ans+=height_diff*length
            st.append(i)
        return ans
                
                
        