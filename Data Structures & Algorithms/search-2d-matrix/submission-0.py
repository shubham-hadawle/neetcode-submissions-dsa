class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search on Rows
        start_m, end_m = 0, len(matrix)-1
        while start_m <= end_m:
            mid_m = (start_m + end_m)//2
            print(mid_m)
            if target < matrix[mid_m][0]: # target < 1st element of the mid_row
                end_m = mid_m - 1
            elif target > matrix[mid_m][-1]: # target > last element of the mid_row
                start_m = mid_m + 1
            else:
                break

        # After the loop, check if the target element actually exists in the matrix
        if not (start_m <= end_m):
            return False
        
        # Setting the value of the target_row
        target_row = (start_m + end_m) // 2
        # Binary Search on Columns
        start_n, end_n = 0, len(matrix[target_row])-1
        while start_n <= end_n:
            mid_n = (start_n + end_n)//2
            print(mid_n)

            if target < matrix[target_row][mid_n]:
                end_n = mid_n - 1
            elif target > matrix[target_row][mid_n]:
                start_n = mid_n + 1
            elif target == matrix[target_row][mid_n]:
                return True

        return False