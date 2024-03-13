class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        left_count = 0
        right_count = 0
        for ch in s:
            if not ch in set(["(",")"]):
                continue
            elif ch == "(":
                left_count+=1
            else:
                if left_count>0:
                    left_count-=1
                else:
                    right_count+=1
        
        result = set()
        def valid_strings(valid_string_list, left_count, right_count, left_used, right_used, index):
            if index == len(s):
                
                if left_count == 0 and right_count == 0 and left_used == right_used:
                    new_list = valid_string_list
                    result.add("".join(new_list))
            
            elif s[index] == "(":
                if left_count > 0:
                    valid_strings(valid_string_list, left_count-1, right_count, left_used, right_used, index+1)
                
                valid_string_list.append(s[index])
                valid_strings(valid_string_list, left_count, right_count, left_used+1, right_used, index+1)
                valid_string_list.pop()
                    
            elif s[index] == ")":
                if right_count > 0:
                    valid_strings(valid_string_list, left_count, right_count-1, left_used, right_used, index+1)
                if left_used > right_used:
                    valid_string_list.append(s[index])
                    valid_strings(valid_string_list, left_count, right_count, left_used, right_used+1, index+1)
                    valid_string_list.pop()
                    
            else:
                valid_string_list.append(s[index])
                valid_strings(valid_string_list, left_count, right_count, left_used, right_used, index+1)
                valid_string_list.pop()
                
            
        valid_strings([], left_count, right_count, 0, 0, 0)
        return list(result)
                
                    
                
                
        