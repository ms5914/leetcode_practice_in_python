class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        i = 0
        neg_index = 0
        result = []
        while i<len(nums) and nums[i]<0:
            neg_index+=1
            i+=1
        
        i = neg_index-1
        j = neg_index

        while i>=0 and j<len(nums):
            if abs(nums[i]) < abs(nums[j]):
                result.append(nums[i]*nums[i])
                i-=1
            
            else:
                result.append(nums[j]*nums[j])
                j+=1

        while i>=0:
            result.append(nums[i]*nums[i])
            i-=1
        while j<len(nums):
            result.append(nums[j]*nums[j])
            j+=1
        return result
        

# Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

# For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

# Algorithm

# We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive direction, and another i in the negative direction.

# Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.


        


        