class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxMax = nums[0]
        curMax = 0

        for n in nums:
            curMax = max(curMax, 0)
            curMax += n
            maxMax = max(maxMax, curMax)
        
        return maxMax


        