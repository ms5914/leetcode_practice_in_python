class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        dq = deque()
        # for i in range(k):
        #     while dq and nums[dq[-1]]<nums[i]:
        #         dq.pop()
        #     dq.append(i)
        
        # result.append(nums[dq[0]])

        for j in range(0, len(nums)):
            
            while dq and dq[0] <= j-k:
                dq.popleft()
            
            while dq and nums[dq[-1]]<nums[j]:
                dq.pop()
            
            dq.append(j)
            if j>=k-1:
                result.append(nums[dq[0]])
        
        return result
            
        

       #SLIDING WINDOW

#        In general, whenever we encounter a new element x, we want to discard all elements that are less than x before adding x. Let's say we currently have [63, 15, 8, 3] and we encounter 12. Any future window with 8 or 3 will also contain 12, so we can discard them. After discarding them and adding 12, we have [63, 15, 12]. As you can see, we keep elements in descending order.

# To perform these operations, we can use a monotonic queue as it supports efficient insertion, deletion, and retrieval of elements from the ends of a window. We will implement it with the deque data structure.

#This question can also be done using heap. 
#let every element be in the heap and just remove out of window largest elements in every itertion so that you always get the largest in the current window.

        