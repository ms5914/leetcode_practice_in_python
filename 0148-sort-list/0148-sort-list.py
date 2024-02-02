# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        
        
        def return_mid_node(head):
            if not head.next:
                return head
            slow = head
            fast = head.next.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None   #Remember to do this, setting the end of first list to be none.
            return mid #You're returning the starting node of second list
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            mid = return_mid_node(head)
            first_half = merge_sort(head)
            second_half = merge_sort(mid)
            result_head = merge(first_half, second_half)
            return result_head
        
        def merge(head, mid):
            result = None
            result_head = None
            while head and mid:
                if head.val <= mid.val:
                    if not result:
                        result = head
                        result_head = result
                    else:
                        result.next = head
                        result = result.next
                    head = head.next
                else:
                    if not result:
                        result = mid
                        result_head = result
                    else:
                        result.next = mid
                        result = result.next
                    mid = mid.next
            
            while head:
                result.next = head
                result = result.next
                head = head.next
            
            while mid:
                result.next = mid
                result = result.next
                mid = mid.next
            
            return result_head
        
        return merge_sort(head)
           
            
                
                    
                        
                
            
            
            
                
        
        
                
                
        