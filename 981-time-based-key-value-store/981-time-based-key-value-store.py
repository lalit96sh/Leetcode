class TimeMap:

    def __init__(self):
        self.keys = collections.defaultdict(lambda : [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.keys[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        if not self.keys[key] or self.keys[key][0][0]>timestamp:
            return ""
        
        l = 0
        r = len(self.keys[key])-1
        
        while l<r:
            mid = (l+r+1)//2
            
            if self.keys[key][mid][0]<=timestamp:
                l = mid
            else:
                r = mid-1
        return self.keys[key][l][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)