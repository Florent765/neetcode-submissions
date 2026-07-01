class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        t, b = 0, r - 1

        while t <= b:
            m1 = (t + b) // 2
            if target > matrix[m1][-1]:
                t = m1 + 1
            elif target < matrix[m1][0]:
                b = m1 - 1
            else:
                break

        if not(t <= b):
            return False
        
        m1 = (t + b) // 2
        l, r = 0, c - 1
        while l <= r:
            m2 = (l + r) // 2
            if matrix[m1][m2] == target:
                return True
            if matrix[m1][m2] < target:
                l = m2 + 1
            else:
                r = m2 - 1

        return False
            
            
            
            
            
            