# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        _sum = 0
        
        dummy = ListNode()
        dummy.next = head
        mp = {0: dummy}
        
        node = head
        while node:
            
            _sum +=  node.val
            if _sum in mp:
                prev_node = mp[_sum]
                
                temp = prev_node.next
                temp_sum = _sum
                while temp!=node:
                    temp_sum += temp.val
                    del mp[temp_sum]
                    temp = temp.next
                    
                    
                prev_node.next = node.next
                
            else:
                mp[_sum] = node
                
            node = node.next
        return dummy.next