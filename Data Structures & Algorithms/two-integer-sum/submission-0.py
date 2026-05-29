class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compare = dict()

        for i in range(len(nums)):
            compare[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in compare:
                if i != compare[diff]:
                    return [i, compare[diff]]