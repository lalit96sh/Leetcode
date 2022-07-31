class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        i = 0
        j = len(arr)-1
        
        while i<j:
            mid = (i+j)//2
            
            if arr[mid]<arr[mid+1]:
                i = mid+1
            else:
                j = mid
            
        return i