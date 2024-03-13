class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        useless_left_count = 0
        useless_right_count = 0
        
        #Count the no. of uselss left and right brackets that needs to be removed
        for ch in s:
            if not ch in set(["(",")"]):
                continue
            elif ch == "(":
                useless_left_count+=1
            else:
                if useless_left_count>0:
                    useless_left_count-=1
                else:
                    useless_right_count+=1
        
        
        #bactracking solution to try adding index by index, each index char can be present or not present. Skip ( based on uselss left count left , same for ). Add ")" based on currently used "(" count.
        result = set()
        def valid_strings(valid_string_list, useless_left_count, useless_right_count, left_used, right_used, index):
            if index == len(s):
                #Check if we have the reqd amout of useless ( and ) and left used is equal to right_used
                if useless_left_count == 0 and useless_right_count == 0 and left_used == right_used:
                    new_list = valid_string_list
                    result.add("".join(new_list))
            
            elif s[index] == "(":
                if useless_left_count > 0:
                    valid_strings(valid_string_list, useless_left_count-1, useless_right_count, left_used, right_used, index+1)
                
                valid_string_list.append(s[index])
                valid_strings(valid_string_list, useless_left_count, useless_right_count, left_used+1, right_used, index+1)
                valid_string_list.pop()
                    
            elif s[index] == ")":
                if useless_right_count > 0:
                    valid_strings(valid_string_list, useless_left_count, useless_right_count-1, left_used, right_used, index+1)
                if left_used > right_used:
                    valid_string_list.append(s[index])
                    valid_strings(valid_string_list, useless_left_count, useless_right_count, left_used, right_used+1, index+1)
                    valid_string_list.pop()
                    
            else:
                valid_string_list.append(s[index])
                valid_strings(valid_string_list, useless_left_count, useless_right_count, left_used, right_used, index+1)
                valid_string_list.pop()
                
            
        valid_strings([], useless_left_count, useless_right_count, 0, 0, 0)
        return list(result)
                
                    
                
                
        