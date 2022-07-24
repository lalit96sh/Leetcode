class HitCounter:

    def __init__(self):
        self.window = collections.deque()
        self.allowed_window_size = 300
        

    def hit(self, timestamp: int) -> None:
        # self.clear(timestamp)
        self.window.append(timestamp)
        
    def clear(self, timestamp):
        while self.window and self.window[0]<=timestamp-self.allowed_window_size:
            self.window.popleft()
            

    def getHits(self, timestamp: int) -> int:
        
        self.clear(timestamp)
        return len(self.window)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)