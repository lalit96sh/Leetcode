# class Node:
#     def __init__(self,val=None):
#         self.val = val
#         self.next, self.prev = None,None
# class DLL:
#     def __init__(self):
#         self.head = Node()
#         self.head.next = self.head.prev=self.head
    
#     def remove_link(self,node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
    
#     def add_link_to_front(self,node):
#         node.next = self.head.next
#         node.prev = self.head
        
#         self.head.next = node
#         node.next.prev = node
#     def add_node(self,val):
#         node = Node(val)
#         self.add_link_to_front(node)
#         return Node        
        
    
class RandomizedSet:

    def __init__(self):
        
        self.lookup = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        
        self.lookup[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        
        idx = self.lookup[val]
        last_val = self.list[-1]
        self.lookup[last_val] = idx
        self.list[idx] = last_val
        self.list.pop()
        del self.lookup[val]
        return True 

    def getRandom(self) -> int:
        return random.choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()