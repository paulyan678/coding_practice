class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Row-wise Binary Search to find the potential row
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][n - 1]:
                low = mid + 1
            else:
                # Proceed to Step 2 with this row
                selectedRow = mid
                break
        else:
            # If no row is found, the target is not present
            return False

        # Step 2: Column-wise Binary Search in the selected row
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if target == matrix[selectedRow][mid]:
                return True
            elif target < matrix[selectedRow][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False