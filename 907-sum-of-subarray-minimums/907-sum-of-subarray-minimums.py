class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        st = [-1]
        ans = 0
        arr.append(float("-inf"))
        for i,num in enumerate(arr):
            while st and arr[st[-1]]>num:
                j = st.pop()
                k = st[-1]
                ans+=arr[j]*(i-j)*(j-k)
            st.append(i)
        
        arr.pop()
        return (ans%(10**9+7))
            
            
                
            
        