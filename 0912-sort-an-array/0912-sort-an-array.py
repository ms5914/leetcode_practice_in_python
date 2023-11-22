class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result= []

        max_limit = pow(10,5)+1

        count_list = [0]*max_limit

        for num in nums:
            count_list[num+5*pow(10,4)]+=1

        for i in range(len(count_list)):
            for j in range(count_list[i]):
                result.append(i-5*pow(10,4))

        return result
