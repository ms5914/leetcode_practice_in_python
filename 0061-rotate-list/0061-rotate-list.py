# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head #Do check base case
        
        def find_length(head):
            list_len = 0
            while head:
                head = head.next
                list_len+=1
            return list_len
        
        k = k%find_length(head)
        if k==0:  #Do check base case, if zero rotations return the same head
            return head
            
        fast = head
        count = 0

        while count<k:
            fast = fast.next
            count+=1

        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        rotate_node = slow.next
        slow.next = None
        fast.next = head


        return rotate_node
                
            
            
            