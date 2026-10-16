class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to find indices of number a and b such that 
        # their sum equals the target 

        # 1. brute-force O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         total = nums[i] + nums[j]
        #         if total == target:
        #             return [i, j]

        # 2. efficient O(n) using two pointers 
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num 
            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[num] = i


        

