class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False 
        
        def binarySearch(array, low, high):
            middle = (low + high) // 2
            if low > high:
                return False
            elif target > array[middle]:
                low = middle + 1 
                return binarySearch(array, low, high)
            elif target < array[middle]:
                high = middle - 1
                return binarySearch(array, low, high)
            else:
                return True

        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True 
            elif i + 1 == len(matrix):
                return binarySearch(matrix[i], 0, len(matrix[i])-1) # at ith row
            elif matrix[i][0] < target < matrix[i+1][0]:
                return binarySearch(matrix[i], 0, len(matrix[i])-1) # at ith row 
            else: 
                continue 
             

