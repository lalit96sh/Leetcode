# import collections
class Node:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None
        
class DLL:
    def __init__(self):
        self._size = 0
        self.head = Node()
        self.head.next = self.head.prev = self.head
    
    def __len__(self):
        return self._size
    
    def append(self,node):
        
        node.next=self.head.next
        node.prev = self.head
        
        self.head.next = node
        node.next.prev = node
        
        self._size+=1
    
    def pop(self,node=None):
        
        if self._size==0:
            return None
        if not node:
            node = self.head.prev
        
        node.next.prev = node.prev
        node.prev.next = node.next
        
        self._size-=1
        
        return node
        
        
        
class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.size = 0
        
        self.lookup = {}
        self.freq_lookup = collections.defaultdict(DLL)
        self.min_freq = 0
      
    def _update(self,node):
        
        frq = node.freq
        self.freq_lookup[frq].pop(node)
        node.freq +=1
        if frq==self.min_freq and len(self.freq_lookup[frq])==0:
            self.min_freq+=1
        
        self.freq_lookup[node.freq].append(node)
        
        
        

    def get(self, key: int):
        if key not in self.lookup:
            return -1
        node = self.lookup.get(key)
        self._update(node)
        return node.val

        

    def put(self, key: int, value: int):
        if self.capacity==0:
            return
        if key in self.lookup:
            node = self.lookup.get(key)
            node.val = value
            self._update(node)
        else:
            if self.size==self.capacity:
                popped = self.freq_lookup[self.min_freq].pop()
                del self.lookup[popped.key]
                self.size-=1
            
            node = Node(key,value)
            self.lookup[key] = node
            self.min_freq = 1
            self.freq_lookup[1].append(node)
            self.size+=1
            