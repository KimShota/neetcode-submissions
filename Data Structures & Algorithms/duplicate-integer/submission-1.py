class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hello = set()

        for num in nums:
            if num in hello:
                return True 
            hello.add(num)
        
        return False
