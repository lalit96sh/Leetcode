# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        for i in range(n):
            head = head.next
        while head:
            head=head.next
            prev=prev.next
        
        prev.next = prev.next.next
        
        return dummy.next