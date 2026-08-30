class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
            0 1 2 3 4 5 6 7 8
        0
        1
        2
        3
        4
        5
        6
        7
        8
        
        '''
        num_set = set()

        # go through each row
        for i in range(0, len(board), 1):
            for j in range(0, len(board[i]), 1):
                if board[i][j] != '.':
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
            num_set.clear()
            
        # go through each column
        for j in range(0, len(board[0]), 1):
            for i in range(0, len(board), 1):
                if board[i][j] != '.':
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
            num_set.clear()

        # go through each 3x3 grid
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                for k in range(0, 3, 1):
                    for l in range(0, 3, 1):
                        if board[i+k][j+l] != '.':
                            if board[i+k][j+l] in num_set:
                                return False
                            num_set.add(board[i+k][j+l])
                num_set.clear()

        return True

        