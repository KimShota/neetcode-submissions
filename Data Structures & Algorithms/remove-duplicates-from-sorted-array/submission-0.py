class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 
        right = 1 
        count = 1

        while right <= len(nums) - 1:
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1 
                count += 1
            right += 1 
        
        return count 