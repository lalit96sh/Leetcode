class Node:
    def __init__(self,freq=None):
        self.freq = freq
        self.values = set()
        self.size = 0
        self.next = self.prev = None
    def insert(self,val):
        self.values.add(val)
        self.size+=1
    def remove(self,val):
        self.values.discard(val)
        self.size-=1
    def pop_and_append_any(self):
        val = self.values.pop()
        self.values.add(val)
        return val

    def __len__(self):
        return self.size

class DLL:
    def __init__(self):
        self.head = Node(0)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0
    
    def delete(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size+=1
    
    def remove_val(self,node,val):
        node.remove(val)
        if not len(node):
            self.delete(node)
            return True
        return False
    
    def add_next(self,first,node):
        
        node.next = first.next
        node.prev = first
        
        node.next.prev = node
        node.prev.next = node
        self.size+=1
        
    
    def add_node(self,prev,node,change):
        
        if not prev:
            prev = self.head
        
        if change==1:
            self.add_next(prev,node)
        else:
            self.add_next(prev.prev,node)
    
    def get_max(self):
        if not self.size:
            return ""
        node = self.head.prev
        return node.pop_and_append_any()
    def get_min(self):
        if not self.size:
            return ""
        node = self.head.next
        return node.pop_and_append_any()

class AllOne:

    def __init__(self):
        self.val_freq_map = collections.defaultdict(int)
        self.freq_node_map = collections.defaultdict(Node)
        self.dll = DLL()
    
    def update(self,key,change):
        old_freq = self.val_freq_map[key]
        
        new_freq = old_freq+change
        
        if new_freq:
            node = self.freq_node_map[new_freq]
            node.insert(key)
            old_node = None if old_freq==0 else self.freq_node_map[old_freq]
            if node.next is None:
                self.dll.add_node(old_node,node,change)
            self.val_freq_map[key] = new_freq
        else:
            del self.val_freq_map[key]
            
        
        if old_freq:
            node = self.freq_node_map[old_freq]
            if self.dll.remove_val(node,key):
                del self.freq_node_map[old_freq]
        
        

    def inc(self, key: str) -> None:
        self.update(key,1)
        

    def dec(self, key: str) -> None:
        self.update(key,-1)
        

    def getMaxKey(self) -> str:
        return self.dll.get_max()   

    def getMinKey(self) -> str:
        return self.dll.get_min()  
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()