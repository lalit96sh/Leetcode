# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.cur_pointer = 0
        self.read4_pointer = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i<n:
            if self.read4_pointer==self.cur_pointer:
                self.cur_pointer = 0
                self.read4_pointer = read4(self.buf4)
                if self.read4_pointer==0:
                    break
            buf[i] = self.buf4[self.cur_pointer]
            self.cur_pointer+=1
            i+=1
        
        return i
        
        