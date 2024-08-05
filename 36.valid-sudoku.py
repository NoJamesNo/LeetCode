#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = set()
        col_dict = {}
        sub_dict = {}

        for i in range(len(board)):
            for j in range(len(board[i])):                
                # stuff for row detection
                if board[i][j] in row_dict:
                    if board[i][j] != ".":
                        return False
                else:
                    row_dict.add(board[i][j])
                    
                # stuff for column detection
                if board[i][j] in col_dict.get(j,set()):
                    if board[i][j] != ".":
                        return False
                else:
                    col_dict.setdefault(j, set()).add(board[i][j])
                    
                # stuff for sub box detection
                if board[i][j] in sub_dict.get(tuple([int(i/3),int(j/3)]),set()):
                    if board[i][j] != ".":
                        return False
                else:
                    sub_dict.setdefault(tuple([int(i/3),int(j/3)]), set()).add(board[i][j])
            print(row_dict)
            row_dict = set()
                
        return True
    
#note you can do integer divison with //
                
        
# @lc code=end

