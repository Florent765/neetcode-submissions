class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            s = set()
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                if val in s:
                    return False
                s.add(val)

        for i in range(n):
            s = set()
            for j in range(n):
                val = board[j][i]
                if val == '.':
                    continue
                if val in s:
                    return False
                s.add(val)

        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                
                box_id = (i // 3) * 3 + (j // 3)

                if val in boxes[box_id]:
                    return False
                
                boxes[box_id].add(val)

        return True
        
        return True