class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def find_subset(curr_index, candidate):
            if curr_index == n:
                result.append(list(candidate))
            
            else:
                candidate.append(nums[curr_index])
                find_subset(curr_index+1, candidate)
                candidate.pop()
                find_subset(curr_index+1, candidate)
        find_subset(0, [])
        return result