class Node:
    
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.next = self.prev = None
        
class DLL:
    
    def __init__(self):
        self.head = Node()
        self.head.next = self.head.prev = self.head
        
    def delete_link(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def link_node_to_front(self,node):
        
        node.next = self.head.next
        node.prev = self.head
        
        node.prev.next = node
        node.next.prev = node
        
    def move_node_to_front(self,node):
        self.delete_link(node)
        self.link_node_to_front(node)
        
    def pop_node(self):
        node = self.head.prev
        self.delete_link(node)
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dll = DLL()
        self.lookup = {}

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        self.dll.move_node_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.dll.move_node_to_front(node)
        else:
            if self.size == self.capacity:
                self.size-=1
                node = self.dll.pop_node()
                del self.lookup[node.key]
            
            self.size+=1
            
            node = Node(key,value)
            self.dll.link_node_to_front(node)
            self.lookup[key] = node
            
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)