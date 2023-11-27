class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A)-1
        total = len(A)+len(B)
        
        while l<=r+1: #Do it till while True to avoid confusion : Since median is bound to exist somewhere. 
            print(l,r)
            a_left_index = r+(l-r)//2
            b_left_index = (total//2)-a_left_index-2
            
            
            a_left = A[a_left_index] if a_left_index>=0 else -1*float("inf")
            a_right = A[a_left_index+1] if  a_left_index+1<len(A) else float("inf")
            b_left = B[b_left_index] if b_left_index>=0 else -1*float("inf")
            b_right = B[b_left_index+1] if  b_left_index+1<len(B) else float("inf")
            
            if a_left<=b_right and b_left<=a_right:
                if total%2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left,b_left)+min(a_right, b_right))/2
            elif b_left>a_right:
                l = a_left_index+1
            else:
                r = a_left_index-1
        
        
                
            
            
        
        
            
        