class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]


        common_str = strs[0]
        for word in strs[1:]:
            i = 0
            if common_str == "":
                return ""
            while i<len(word) and i<len(common_str):
                if word[i] == common_str[i]:
                    i+=1
                else:
                    break
            common_str=common_str[:i]
        
        return common_str



        