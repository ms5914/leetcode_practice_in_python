class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for string in strings:
            curr = []
            for a,b in zip(string, string[1:]):
                remainder = (ord(b)-ord(a)+26)%26
                curr.append(remainder)
            mapp[tuple(curr)].append(string)
        return list(mapp.values())