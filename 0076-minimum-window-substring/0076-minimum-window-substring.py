class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0,0
        if not s:
            return ""
        if len(s)<len(t):
            return ""
        
        s_dict = defaultdict(int)
        t_dict = Counter(t)
        matched = 0
        shortest_substr = [float("inf"),0,0]
        while j<len(s):
            s_dict[s[j]]+=1
            if s[j] in t_dict and s_dict[s[j]] == t_dict[s[j]]:
                matched+=1
            while matched == len(t_dict):
                 if shortest_substr[0] > j-i+1:
                    shortest_substr= [j-i+1, i,j]
                 s_dict[s[i]]-=1
                 if s[i] in t_dict and s_dict[s[i]]<t_dict[s[i]]:
                    matched-=1
                 i+=1
            j+=1
        return s[shortest_substr[1]:shortest_substr[2]+1] if shortest_substr[0] != float("inf") else ""



