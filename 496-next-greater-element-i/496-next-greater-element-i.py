class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st = []
        for v in nums2:
            while st and st[-1]<v:
                mp[st.pop()] = v
            st.append(v)
        return [mp.get(n,-1) for n in nums1]