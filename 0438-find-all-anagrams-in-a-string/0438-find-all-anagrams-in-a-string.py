class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []

        i,j = 0,0
        t_map = Counter(p)
        s_map = defaultdict(int)
        result=[]

        max_match = 0
        while j<len(s):
            s_map[s[j]]+=1
            if j-i+1 == len(p):
                if s_map == t_map:
                    result.append(i)
                s_map[s[i]]-=1
                if s_map[s[i]] == 0:
                    del s_map[s[i]]
                i+=1
            j+=1
        return result


