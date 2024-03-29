class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # keep track of found differences
        first_diff = -1
        second_diff = -1
        
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                if first_diff == -1:
                    first_diff = idx
                elif second_diff == -1:
                    second_diff = idx
                else:
                    # found more than two differences
                    return False
        
        # if differences are equal in cross then strings would become equal
        return s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff]
        