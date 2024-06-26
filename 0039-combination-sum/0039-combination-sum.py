

# So there are two ways of doing this problem:
#     Method 1
#     1. Seeing each number in the list and seeing it can either be taken multiple times
#     2. Not taken at all 
    
#     Method 2
#     Incrementally build combinations and make sure for every recursion you are starting with start and not 0. It helps finding combinations and not permutations 
    
    

#Method 1
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        s = 0
        combination = []
        self.findCombinations(result,0, s, target, [], candidates)
        return result
    
    def findCombinations(self, result, i, s, target, combination, candidates):
        print(combination)
        if s == target:
            result.append(combination)
        elif s>target:
            return
        elif i>len(candidates)-1:
            return
        else:
            self.findCombinations(result, i, s+candidates[i], target,combination+[candidates[i]], candidates )
            self.findCombinations(result, i+1, s, target, combination, candidates)


#Method 2
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []
#         combination=[]
#         running_sum = 0
#         self.find_combinations(combination, running_sum, result, target, 0, candidates)
#         return result
    
#     def find_combinations(self,combination, running_sum, result, target, start, candidates):
#         if running_sum == target:
#             result.append(list(combination))
        
#         if running_sum > target:
#             return
        
#         else:
#             for i in range(start, len(candidates)):
#                 combination.append(candidates[i])
#                 self.find_combinations(combination, running_sum+candidates[i],result,target, i, candidates)
#                 combination.pop()
        
    
                
            
        
        
        
        
# Responding to an old comment, but to add on my interpretation, I don't think backtracking generally intrinsically handles this, though the logic in this particular solution for this question obviously had to be modified to do this.

# To be explicit and elaborating on @suutar 's response, instantiating i in the for loop to be start rather than 0 is what is handling this "deduplication":
# for (int i = start; i < candidates.length; ++i) {

# If we did not have this and instantiated i to be 0 instead, we would get all the permutations that lead to this sum, not combinations.

# I agree that this is a relatively subtle point that is not explicitly explained in either the written explanation or the inline comment.
        