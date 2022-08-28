class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from heapq import heappop,heappush
        h = []
        counter = Counter(nums)
        mx = max(counter.values())
        
        
        bucket = collections.defaultdict(list)
        
        for key in counter:
            bucket[counter[key]].append(key)
        ans = []
        kk = k
        for i in range(mx,0,-1):
            if k<=0:
                break
            k-=len(bucket[i])
            ans.extend(bucket[i])
            
        return ans[-kk:]