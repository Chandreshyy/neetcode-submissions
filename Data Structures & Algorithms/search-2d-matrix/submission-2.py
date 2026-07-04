
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        l, h = 0, m*n - 1

        while l <= h:
            mid = l + (h-l)//2
            i = mid//n
            j = mid%n
            # print(mid, i, j)
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                h = mid - 1
            else:
                l = mid + 1
        
        return False
        