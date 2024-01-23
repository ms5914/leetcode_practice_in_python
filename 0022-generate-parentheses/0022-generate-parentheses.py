class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def create_combination(candidate, n_left, n_right):
            if n_left == n_right == n:
                result.append("".join(candidate))
            
            else:
                if not candidate:
                    candidate.append("(")
                    create_combination(candidate, n_left+1, n_right)
                    candidate.pop()
                    
                else:
                    if n_left>n_right:
                        candidate.append(")")
                        create_combination(candidate, n_left, n_right+1)
                        candidate.pop()
                    if n_left<n:
                        candidate.append("(")
                        create_combination(candidate, n_left+1, n_right)
                        candidate.pop()
        
        create_combination([], 0, 0)
        return result
                
                        
                    
            
            
                
        
        