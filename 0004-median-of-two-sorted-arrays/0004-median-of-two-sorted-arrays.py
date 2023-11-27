class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #The idea is to excecute binary search on the shorter array to figure out how many elements in the smaller array will be a part of lower half in the combined sorted array. 
        
        #If you forget the explanation watch this video:
# https://www.youtube.com/watch?app=desktop&v=q6IEA26hvXc&ab_channel=NeetCode

    
        
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A)-1
        total = len(A)+len(B)
        
        while l<=r+1: #Do it till while True to avoid confusion : Since median is bound to exist somewhere. 
            print(l,r)
            a_left_index = r+(l-r)//2 #Assume array till this index in A will be a part of lower half in the combined sorted array
            b_left_index = (total//2)-a_left_index-2 #based on total count of numbers we know how many elements should be there in lower half so rest of elements will be from B array.
            
            
            #Handling edge cases when we are considering 0 elements in either A or B
            a_left = A[a_left_index] if a_left_index>=0 else -1*float("inf")
            a_right = A[a_left_index+1] if  a_left_index+1<len(A) else float("inf")
            b_left = B[b_left_index] if b_left_index>=0 else -1*float("inf")
            b_right = B[b_left_index+1] if  b_left_index+1<len(B) else float("inf")
            
            if a_left<=b_right and b_left<=a_right: #Partitioning is correct and these are indeed the elements in first half of the array. 
                if total%2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left,b_left)+min(a_right, b_right))/2
            elif b_left>a_right: 
                #i.e there should be more elements from array A instead of B since b_left >s_right
                l = a_left_index+1
            else:   
                #i.e there should be more elements from array B instead of A since a_left > b_right
                r = a_left_index-1
        
        
                
            
            
        
        
            
        