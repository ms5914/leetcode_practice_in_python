# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A = nums1
#         B = nums2
#         if len(B) < len(A):
#             A, B = B, A
        
#         l = 0
#         r = len(A)-1
#         total = len(A)+len(B)
        
#         while l<=r:
            
#             a_left_index = (l+r)//2
#             b_left_index = (total//2)-a_left_index-2
            
#             a_left = A[a_left_index] if a_left_index>=0 else -1*float("inf")
#             a_right = A[a_left_index+1] if  a_left_index+1<len(A) else float("inf")
#             b_left = A[b_left_index] if b_left_index>=0 else -1*float("inf")
#             b_right = A[b_left_index+1] if  b_left_index+1<len(B) else float("inf")
            
#             if a_left<=b_right and b_left<=a_right:
#                 if total%2:
#                     return max(a_left, b_left)
#                 else:
#                     return (max(a_left,b_left)+min(a_right, b_right))/2
#             elif a_left > b_right:
#                 r = a_left_index - 1
#             else:
#                 l = a_left_index + 1
                # Time: log(min(n, m))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            
            
        
        
            
        