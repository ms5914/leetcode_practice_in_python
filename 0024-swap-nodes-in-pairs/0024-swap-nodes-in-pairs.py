# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = self.swapPairs(head.next.next)
        
        next_node = head.next
        curr_node = head
        
        next_node.next = curr_node
        curr_node.next = node
        head = next_node
        
        return head
        
        
        
        