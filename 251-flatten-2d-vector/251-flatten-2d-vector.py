class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        
        self.inner = 0
        self.outer = 0
        
    def preprocess(self):
        while self.outer<len(self.vec) and len(self.vec[self.outer])==self.inner:
            self.inner=0
            self.outer+=1

    def next(self) -> int:
        self.preprocess()
        
        val =  self.vec[self.outer][self.inner]
        self.inner+=1
        return val

    def hasNext(self) -> bool:
        
        self.preprocess()
        return self.outer<len(self.vec)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()