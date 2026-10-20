class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        subsets, curset = [], []
        self.helper(i, nums, subsets, curset)
        return subsets 

    def helper(self, i, nums, subsets, curset):
        if i == len(nums):
            return subsets.append(curset.copy())

        curset.append(nums[i])
        self.helper(i + 1, nums, subsets, curset)
        curset.pop()

        self.helper(i + 1, nums, subsets, curset)
    

        