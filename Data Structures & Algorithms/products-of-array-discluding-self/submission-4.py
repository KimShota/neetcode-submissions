class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n 
        result = [1] * n 

        for i in range(len(nums)):
            if i == 0:
                continue 

            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        return result
