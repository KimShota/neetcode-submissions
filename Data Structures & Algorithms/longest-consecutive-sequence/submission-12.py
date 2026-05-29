class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_count = 1
        current = 1
        
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                current += 1
                if current > max_count:
                    max_count = current
            elif nums[i+1] == nums[i]:
                continue
            else:
                current = 1
        
        return max_count