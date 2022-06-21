class RandomizedCollection:

    def __init__(self):
        
        self.lookup = collections.defaultdict(set)
        self.list = []
        

    def insert(self, val: int) -> bool:
        rvalue = True
        if val in self.lookup:
            rvalue = False
        
        self.lookup[val].add(len(self.list))
        self.list.append(val)
        return rvalue
    def get_first_of_set(self,s):
        for _ in s:
            return _

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        n = len(self.list)
        last = self.list[-1]
        idx = self.lookup[val].pop()
        
        self.list[idx] = last
        
        self.lookup[last].add(idx)
        self.lookup[last].remove(n-1)
        self.list.pop()
        
        
#         last_val = self.list[-1]
#         last_index = len(self.list)-1
#         self.lookup[last_val].remove(last_index)
        
#         if last_val!=val:
#             val_index = self.lookup[val].pop()
#             self.list[val_index] = last_val
#             self.lookup[last_val].add(val_index)
        
        if not self.lookup[val]:
            del self.lookup[val]
        
        return True 

    def getRandom(self) -> int:
        # print(self.list)
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()