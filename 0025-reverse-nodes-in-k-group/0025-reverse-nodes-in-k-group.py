# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        def find_len(head):
            list_len = 0
            while head:
                list_len+=1
                head = head.next
            return list_len
        
        #Find the number of times the reversal has to happen
        num_reversals = find_len(head)//k
        count = 0
        current = head
        
        #The node where previous reversed list ends
        prev_end = None
        
        #Start of the full list, set when first set of nodes are reversed
        start = None
        
        
        while count<num_reversals:
            node_count = 0
            prev = None
            next_node = None
            
            #For every k set of nodes reverse them as separate linked list that ends at None
            while node_count<k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                node_count+=1

            #Start is set for first set of k nodes
            if not start:
                start = prev
            
            #Set the next of the end node of prev set of k nodes that were reversed
            if prev_end:
                prev_end.next = prev
            
            #Set the prev_end for the current set of k nodes so that it can be set correctly for next set of nodes. 
            while prev.next:
                prev = prev.next
            prev_end = prev
            count+=1

        #If there are still some nodes left that cannot be reversed, set the previous ending nodes next as current
        if current:
            prev_end.next = current
        
        return start

            
                
            