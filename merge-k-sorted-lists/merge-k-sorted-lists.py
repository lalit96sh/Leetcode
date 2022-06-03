# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        hp = []
        from heapq import heappush,heappop
        
        mp = collections.defaultdict(list)
        
        for l in lists:
            if not l or l.val is None:
                continue
            mp[l.val].append(l)
            heappush(hp,(l.val))
            
        dummy = cur = ListNode()
        while hp:
            _ = heappop(hp)
            
            node = mp[_].pop()
            cur.next = node
            cur = cur.next
            
            if node.next:
                mp[node.next.val].append(node.next)
                heappush(hp,(node.next.val))
        return dummy.next
            
        