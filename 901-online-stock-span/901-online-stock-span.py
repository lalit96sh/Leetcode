class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.output = []
        self.min = float("inf")
        

    def next(self, price: int) -> int:
        if price<self.min:
            self.stocks.append(price)
            self.min = price
            self.output.append(1)
            return 1
        d = 1
        
        while d<=len(self.stocks) and self.stocks[-d]<=price:
            d+=self.output[-d]
        
        self.stocks.append(price)    
        self.output.append(d)
        return d
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)