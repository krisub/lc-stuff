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
        

        dot_count = 0
        num_set = set()

        # go through each row
        for i in range(0, len(board), 1):
            for j in range(0, len(board[i]), 1):
                if board[i][j] == '.':
                    dot_count += 1
                else:
                    print(f"loop 1, i is {i}, j is {j}, board[i][j] is {board[i][j]}")
                    num_set.add(board[i][j])
            if len(board)-dot_count > len(num_set):
                return False
            print()
            dot_count = 0
            num_set = set()
            
        # go through each column
        for j in range(0, len(board[0]), 1):
            for i in range(0, len(board), 1):
                if board[i][j] == '.':
                    dot_count += 1
                else:
                    print(f"loop 2, i is {i}, j is {j}, board[i][j] is {board[i][j]}")
                    num_set.add(board[i][j])
            if len(board[0])-dot_count > len(num_set):
                return False
            print()
            dot_count = 0
            num_set = set()

        # go through each 3x3 grid
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                for k in range(0, 3, 1):
                    for l in range(0, 3, 1):
                        if board[i+k][j+l] == '.':
                            dot_count += 1
                        else:
                            print(f"loop 3, i is {i}, j is {j}, k is {k}, l is {l} board[i+k][j+l] is {board[i+k][j+l]}")
                            num_set.add(board[i+k][j+l])
                print(f"dot count is {dot_count} and len(num_set) is {len(num_set)}")
                if len(board)-dot_count > len(num_set):
                    return False
                print()
                dot_count = 0
                num_set = set()

        return True

        