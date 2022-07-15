class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        mp = {}
        mx = max(arr2)
        for i,n in enumerate(arr2):
            mp[n] = i
        
        
        arr1.sort(key=lambda x: mp[x] if x in mp else mx+1+x)
        return arr1
        
        