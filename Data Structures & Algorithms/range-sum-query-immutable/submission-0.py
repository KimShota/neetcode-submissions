class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        total = 0
        for num in nums:
            total += num 
            self.arr.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.arr[right]
        prefixLeft = self.arr[left - 1] if left > 0 else 0
        return prefixRight - prefixLeft
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)