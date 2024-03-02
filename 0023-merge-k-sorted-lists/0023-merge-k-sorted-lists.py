# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        list_heap = []
        for li in lists:
            if li:
                heapq.heappush(list_heap,li)
        
        dummy = ListNode(-1)
        current = dummy
        
        while list_heap:
            li = heapq.heappop(list_heap)
            current.next = li
            current = current.next
            if li.next:
                heapq.heappush(list_heap, li.next)
        return dummy.next
                
        
        
                
                

        