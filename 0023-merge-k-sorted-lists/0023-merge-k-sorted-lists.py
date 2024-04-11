# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        list_heap = []
        for i,li in enumerate(lists):
            if li:
                heapq.heappush(list_heap,(li.val,i, li))
        
        dummy = ListNode(-1)
        current = dummy
        
        while list_heap:
            val,i, li = heapq.heappop(list_heap)
            current.next =li
            current = current.next
            if li.next:
                heapq.heappush(list_heap, (li.next.val,i,li.next))
        return dummy.next
    
    #TC: O(NlogK) N:Total number of nodes K: Total num of lists
    #SC: O(K) heap and O(N) to create a new ll
    

    
    

#Optimized approach : Merge lists two at a time TC: O(NlogK) SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval])
#             interval *= 2

#         return lists[0] if amount > 0 else None

#     def merge2Lists(self, l1, l2):
#         head = point = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
#                 l2 = l1
#                 l1 = point.next.next
#             point = point.next

#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1

#         return head.next
                
        
        
                
                

        