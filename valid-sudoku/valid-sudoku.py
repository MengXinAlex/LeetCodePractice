import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # we need to check column, row and each boxs
        
        board = np.array(board)
        
        def check_col(board):
            for i in range(board.shape[0]):
                temp = [j for j in board[i, :] if j != '.']
                if len(set(temp)) != len(list(temp)):
                    return False
            return True
            
        def check_row(board):
            for i in range(board.shape[1]):
                temp = [j for j in board[:, i] if j != '.']
                if len(set(temp)) != len(list(temp)):
                    return False
            return True
            
        def check_box(board):
            for i in range(0, board.shape[1], 3):
                for j in range(0, board.shape[1], 3):
                    sub_box = board[i:i+3, j:j+3]
                    sub_box = list(itertools.chain.from_iterable(sub_box))
                    tmp_list = [val for val in sub_box if val != '.']

                    if len(set(tmp_list)) != len(list(tmp_list)):
                        return False
            return True
    
        return check_col(board) and check_row(board) and check_box(board)
        