from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(compare), reverse=True)
        result = "".join(list(map(lambda x: str(x), nums)))
         
        return "0" if result[0] == "0" else result


def compare(a, b)-> int:
    return int(str(a)+str(b)) - int(str(b)+str(a))