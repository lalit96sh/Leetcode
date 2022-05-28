# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_mid(node):
            
            prev = t1 = t2 = node
            while t2 and t2.next:
                prev = t1
                t1 = t1.next
                t2 = t2.next.next
            
            return prev,t1
        
        def merge(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            dummy = prev = ListNode()
            
            while l1 and l2:
                
                if l1.val<=l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            
            prev.next = l1 if l1 else l2
            
            return dummy.next
        
        def sort_list(head):
            
            if not head or not head.next:
                return head
            
            prev,head2 = get_mid(head)
            
            prev.next = None
            
            return merge(sort_list(head),sort_list(head2))
        
        return sort_list(head)
            