class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # left_prod, right_prod = [None]*len(nums), [None]*len(nums)
        # left_prod[0], right_prod[len(nums)-1] = 1,1
        # result=[]
         
        # for i in range(1, len(nums)):
        #     left_prod[i] = left_prod[i-1]*nums[i-1]
        
        # for j in range(len(nums)-2,-1,-1):
        #     right_prod[j] = right_prod[j+1]*nums[j+1]

        # print(left_prod)
        # print(right_prod)
        # for k in range(len(nums)):
        #     result.append(left_prod[k]*right_prod[k])
        

        # return result


        #Constant space approach
        ans = [None]*len(nums)
        ans[0]= 1
        running_prod = 1

        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i]*running_prod
            running_prod *=nums[i]
        
        return ans
        

        
        
        








        

        





        