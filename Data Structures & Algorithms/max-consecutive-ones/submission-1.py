class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0
        for num in nums:
            if num == 1:
                counter += 1
                if max_counter < counter:
                    max_counter = counter
            else:
                counter = 0

        return max_counter 
            
        