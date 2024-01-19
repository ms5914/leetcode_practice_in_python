class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        result = []
        if not digits:
            return result
        n  = len(digits)
        
        
        def find_combinations(candidate, index):
            if index == n:
                result.append("".join(candidate))
            else:
                for value in hm[int(digits[index])]:
                    candidate.append(value)
                    find_combinations(candidate, index+1)
                    candidate.pop()
        
        find_combinations([], 0)
        return result