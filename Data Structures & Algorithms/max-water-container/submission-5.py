class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 

        maxA = 0 
        curA = 0
        left = 0 
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            curA = height * width 
            maxA = max(curA, maxA)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1 

        return maxA
