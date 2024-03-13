import random as rnd
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] = w[i-1]+w[i]
        self.w = w

    def pickIndex(self) -> int:
        index = bisect.bisect_left(self.w,rnd.randint(1, self.w[len(self.w)-1]))
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()