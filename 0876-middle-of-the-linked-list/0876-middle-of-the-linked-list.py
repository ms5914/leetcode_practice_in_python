# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        list_len = 0
        temp = head
        while temp:
            list_len+=1
            temp = temp.next
        
        mid = (list_len)//2
        
        itr = 0
        temp1 = head
        while itr<mid:
            temp1 = temp1.next
            itr+=1
        return temp1
        
        
            
            
        
        
        