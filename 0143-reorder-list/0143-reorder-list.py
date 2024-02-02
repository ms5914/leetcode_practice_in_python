# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        
        def print_list(head):
            li =[]
            while head:
                li.append(head.val)
                head = head.next
            print(li)
        
        def reverse_list(head):
            prev = None
            current = head
            next_node = None
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        fast = head.next.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow_next = slow.next
        slow.next = None
        second_half_reversed = reverse_list(slow_next)
        
        even = True
        real_head = head
        next_head = head.next
        
        while next_head:
            if even:
                head.next = second_half_reversed
                second_half_reversed = second_half_reversed.next
                head = head.next
                even = False
            else:
                head.next = next_head
                next_head = next_head.next
                head = head.next
                even = True

        
        while second_half_reversed:
            head.next = second_half_reversed
            second_half_reversed = second_half_reversed.next
            head = head.next
        
        
                
                
                
                
                
            
        
        
            
            
            
        
        
        
    
    
                
                
                
                
        