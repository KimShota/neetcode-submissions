class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        hashSet = set(nums)
        current = 1
        max_count = 1

        for n in nums:
            if n - 1 not in hashSet:
                while True:
                    if n + 1 in hashSet:
                        current += 1
                        n = n + 1
                        max_count = max(current, max_count)
                    else:
                        break
                current = 1
        return max_count



        # if not nums:
        #     return 0

        # nums.sort()
        # max_count = 1
        # current = 1
        
        # for i in range(len(nums) - 1):
        #     if nums[i+1] - nums[i] == 1:
        #         current += 1
        #         if current > max_count:
        #             max_count = current
        #     elif nums[i+1] == nums[i]:
        #         continue
        #     else:
        #         current = 1
        
        # return max_count
