class StockPrice:

    def __init__(self):
        
        self.cur = (float("-inf"),None)
        self.lookup = {}
        self.minheap = []
        self.maxheap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.lookup[timestamp] = price
        heapq.heappush(self.minheap,(price,timestamp))
        heapq.heappush(self.maxheap,(-price,timestamp))
        if timestamp>=self.cur[0]:
            self.cur = (timestamp,price)
        
    def current(self) -> int:
        if self.cur[0]!=float("-inf"):
            return self.cur[1]
        

    def maximum(self) -> int:
        while self.lookup[self.maxheap[0][1]]!=-self.maxheap[0][0]:
            heapq.heappop(self.maxheap)
        return -self.maxheap[0][0]
        

    def minimum(self) -> int:

        while self.lookup[self.minheap[0][1]]!=self.minheap[0][0]:
            heapq.heappop(self.minheap)
        return self.minheap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()