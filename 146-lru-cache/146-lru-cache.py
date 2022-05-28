class LRUCache(object):
    class Node:
        def __init__(self,key=None,val=None):
            self.val = val
            self.key = key
            self.next = None
            self.prev = None
        

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.size = 0
        
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_front(self,node):
        next = self.head.next
        
        
        node.prev = self.head
        node.next = next
        
        self.head.next = node
        next.prev = node
        
    def delete_node(self,node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
    def delete_from_end(self):
        node = self.tail.prev
        del self.dict[node.key]
        self.delete_node(node)

    def add(self,key,val):
        if self.dict.get(key):
            node = self.dict.get(key)
            node.val = val
            self.delete_node(node)
        else:
            self.size+=1
            node = self.Node(key,val)
            self.dict[key]=node
        self.move_to_front(node)
        return node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.dict.get(key):
            node = self.dict.get(key)
            self.delete_node(node)
            self.move_to_front(node)
            return self.dict[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.add(key,value)
        if self.size>self.capacity:
            self.size-=1
            self.delete_from_end()
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)