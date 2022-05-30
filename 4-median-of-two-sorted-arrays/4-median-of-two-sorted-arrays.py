class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        l1 = len(nums1)
        l2 = len(nums2)
        half_count = (l1+l2+1)//2
        is_odd = (l1+l2)%2
        # if not l1:
        #     return nums2[l2/2] if is_odd else (nums2[l2/2]+nums2[(l2/2)+1])/2
        start = 0
        end = l1
        while start<=end:
            mid1 = start + (end-start)//2
            mid2 = half_count-mid1
            
            mxl1 = nums1[mid1-1] if mid1>0 else -float("inf")  
            mnr1 = nums1[mid1] if mid1<l1 else float("inf")
            mxl2 = nums2[mid2-1] if mid2>0 else -float("inf")
            mnr2 = nums2[mid2] if mid2<l2 else float("inf")
            
            if mxl1<=mnr2 and mxl2<=mnr1:
                if is_odd:
                    return max(mxl1,mxl2)
                else:
                    return (max(mxl1,mxl2)+min(mnr1,mnr2))/2.0
            elif mxl1 > mnr2:
                end = mid1-1
            else:
                start=mid1+1
        return None
                
                    
                
        
        
        