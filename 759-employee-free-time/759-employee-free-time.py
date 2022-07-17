"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        start_time = []
        end_time = []
        from heapq import heappop, heappush
        
        times = []
        for sc in schedule:
            for ss in sc:
                s = ss.start
                e = ss.end
                times.append([s,-e])
                
        times.sort()
        
        ans = []
        last_max = float("-inf")
        
        for s,e in times:
            
            if -e<=last_max:
                continue
            if s>last_max:
                ans.append(Interval(last_max,s))
            last_max = -e
        
        return ans[1:]
        