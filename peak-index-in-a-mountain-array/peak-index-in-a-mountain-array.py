class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        i = 0
        j = len(arr)-1
        
        while i<=j:
            mid = (i+j)//2
            
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            
            elif arr[mid-1]<arr[mid]<arr[mid+1]:
                i=mid
            else:
                j=mid
        return -1