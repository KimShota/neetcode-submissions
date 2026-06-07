class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        curPre = 1
        curPost = 1
        output = [0] * len(nums)

        # if nums is None:
        #     return output

        for i in range(len(nums)):
            curPre *= nums[i]
            prefix[i] = curPre

        for i in range(len(nums)-1, -1, -1):
            curPost *= nums[i]
            postfix[i] = curPost

        for i in range(len(nums)):
            if i == 0:
                output[i] = postfix[i + 1]
                continue 
            if i == len(nums) - 1:
                output[i] = prefix[i - 1]
                continue 
            output[i] = prefix[i - 1] * postfix[i + 1]

        return output 


        

        
            
        