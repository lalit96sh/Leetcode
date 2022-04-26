class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mx, mxi = nums[0], 0
        for i,nm in enumerate(nums[1:],1):
            
            if mx<nm:
                mx, mxi = nums[i], i
            
        
        n = len(nums)
        ans = [-1]*n
        j = (mxi+1)%n
        st = []
        while True:
            while st and nums[st[-1]]<nums[j]:
                ans[st.pop()] = nums[j]
            st.append(j)  
            if j==mxi:
                break
            
            j = (j+1)%n
        return ans