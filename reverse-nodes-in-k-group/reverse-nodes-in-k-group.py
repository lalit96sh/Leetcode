# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def helper(head):
            if not head or not head.next:
                return head
            cnt = 0
            prev = None
            cur = head
            while cnt<k and cur:
                
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                cnt+=1
            
            if cnt!=k:
                p = None
                while prev:
                    next = prev.next
                    prev.next = p
                    p = prev
                    prev = next
                return p
                    
            if cur:
                head.next = helper(cur)
            return prev
        return helper(head)