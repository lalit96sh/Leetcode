class Logger:

    def __init__(self):
        self.message_map = collections.defaultdict(lambda : 0)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        prev = self.message_map[message]
        
        if prev<=timestamp:
            self.message_map[message] = timestamp+10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)