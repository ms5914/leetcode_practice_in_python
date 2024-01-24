# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        result = None
        c = 0
        head = None
        
        while l1 and l2:
            s = (l1.val+l2.val+c)%10
            c = (l1.val+l2.val+c)//10
            if not result:
                result = ListNode(s)
                head = result
            else:
                result.next = ListNode(s)
                result = result.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            s = (l1.val+c)%10
            c = (l1.val+c)//10
            result.next = ListNode(s)
            result = result.next
            l1 = l1.next
        
        while l2:
            s = (l2.val+c)%10
            c = (l2.val+c)//10
            result.next = ListNode(s)
            result = result.next
            l2 = l2.next
        
        if c>0:
            result.next = ListNode(c)
            result = result.next
        
        return head
            
            
            
            