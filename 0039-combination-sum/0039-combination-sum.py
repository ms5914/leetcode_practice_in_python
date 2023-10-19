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


        