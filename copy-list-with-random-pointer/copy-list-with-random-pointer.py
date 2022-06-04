"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        
        while cur:
            next = cur.next
            
            node = Node(cur.val)
            cur.next = node
            node.next = next
            
            cur = next
            
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = prev =  head
        newhead = newprev = cur.next
        
        cur = cur.next.next
        while cur:
            
            prev.next = cur
            newprev.next = cur.next
            
            prev = cur
            newprev = cur.next
            cur = cur.next.next
        
        return newhead
        
            
        
        
        