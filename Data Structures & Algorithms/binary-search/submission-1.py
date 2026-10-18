class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        def binarySearch(left, right):
            mid = (left + right) // 2

            if left > right:
                return -1
            
            if nums[mid] > target:
                right = mid - 1 
                return binarySearch(left, right)
            elif nums[mid] < target:
                left = mid + 1
                return binarySearch(left, right)
            else:
                return mid 

        return binarySearch(left, right)