class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from heapq import heappop,heappush
        h = []
        counter = Counter(nums)
        for nm in counter:
            heappush(h,(counter[nm],nm))
            if len(h)>k:
                heappop(h)
        ans = []
        while h:
            ans.append(heappop(h)[1])
        return ans[::-1]