class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Counting Sort because the range is comparatively less
        
        result= []

        max_limit = pow(10,5)+1

        count_list = [0]*max_limit

        for num in nums:
            count_list[num+5*pow(10,4)]+=1

        for i in range(len(count_list)):
            for j in range(count_list[i]):
                result.append(i-5*pow(10,4))

        return result

    
    #Better one using the range of array(min and max elem) as a size for storing the counts

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def counting_sort():
#             # Create the counting hash map.
#             counts = {}
#             # Find the minimum and maximum values in the array.
#             minVal, maxVal = min(nums), max(nums)
#             # Update element's count in the hash map.
#             for val in nums:
#                 counts[val] = counts.get(val, 0) + 1

#             index = 0
#             # Place each element in its correct position in the array.
#             for val in range(minVal, maxVal + 1, 1):
#                 # Append all 'val's together if they exist.
#                 while counts.get(val, 0) > 0:
#                     nums[index] = val
#                     index += 1
#                     counts[val] -= 1

#         counting_sort()
#         return nums