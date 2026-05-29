import math 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        def binarySearch(high, low):
            if low > high:
                return -1

            middle = math.ceil((high + low) / 2)
            if target > nums[middle]:
                low = middle + 1
                return binarySearch(high, low)
            elif target < nums[middle]:
                high = middle - 1
                return binarySearch(high, low)
            else:
                return middle

        return binarySearch(high, low)