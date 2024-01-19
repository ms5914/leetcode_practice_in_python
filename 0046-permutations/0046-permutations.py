class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n = len(nums)
        res = nums
        def find_permutations(res, cur_index):
                if cur_index == n:
                    result.append(list(res))
                for i in range(cur_index,len(nums)):
                    res[cur_index], res[i] = res[i], res[cur_index]
                    find_permutations(res, cur_index+1)
                    res[cur_index], res[i] = res[i], res[cur_index]
        
        find_permutations(res, 0)
        return result

                
        #Time complexity = n*n! -> There are n! permutations and we have to copy over each permutation in the result list
        