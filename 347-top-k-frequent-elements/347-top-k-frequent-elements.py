class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from heapq import heappop,heappush
        h = []
        counter = Counter(nums)
        for nm in counter:
            heappush(h,(-counter[nm],nm))
        ans = []
        for i in range(k):
            ans.append(heappop(h)[1])
        return ans