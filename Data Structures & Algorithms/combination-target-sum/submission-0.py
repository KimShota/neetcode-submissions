class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curset = [], []
        self.helper(0, combs, curset, nums, target)
        return combs
        
    def helper(self, i, combs, curset, nums, target):
        if sum(curset) == target:
            combs.append(curset.copy())
            return 
        elif sum(curset) > target:
            return 

        if i >= len(nums):
            return 

        for j in range(i, len(nums)):
            curset.append(nums[j])
            self.helper(j, combs, curset, nums, target)
            curset.pop()
            
        