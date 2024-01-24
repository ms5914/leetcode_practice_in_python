# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n = n-1
        itr = 0
        fast_ptr = head
        while itr<n:
            fast_ptr = fast_ptr.next
            itr+=1
        
        slow_ptr = head
        prev_ptr = None
        
        while fast_ptr.next!=None:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        if prev_ptr:
            prev_ptr.next = slow_ptr.next
        
        elif not prev_ptr:
            head = head.next
        
        return head
        
        
            