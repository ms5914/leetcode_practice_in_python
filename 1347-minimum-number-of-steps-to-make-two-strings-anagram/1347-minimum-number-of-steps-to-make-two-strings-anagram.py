class Solution:
    def minSteps(self, s: str, t: str) -> int:
        print(Counter(s))
        print(Counter(t))
        print(Counter(s)-Counter(t))
        return sum((Counter(s) - Counter(t)).values())

        