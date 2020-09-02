from collections import defaultdict
from typing import List

'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

'''

N=9
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solveCell(board)

    # 递归解法
    def solveCell(self, board: List[List[str]], lastcell=-1) -> bool:
        for i in range(lastcell + 1, N * N):
            if board[i // N][i % N] == '.':
                row = i // N
                col = i % N
                break
        else:
            return True
        rowSet={i for i in board[row]}
        colSet={board[j][col] for j in range(9)}
        boxSet={board[row//3*3+i][col//3*3+j] for i in range(3) for j in range(3) }
        use={str(i) for i in range(1,10)}-colSet-rowSet-boxSet
        for number in use:
            board[row][col]=number
            if self.solveCell(board,lastcell=row*N+col):
                return True
        board[row][col] = '.'
        return False

    # 判断数独是否有效
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            valid_row = set()
            valid_col=set()
            valid_sqr = set()
            for j in range(9):
                if board[i][j]!="." :
                    if board[i][j] in valid_row:
                        return False
                    valid_row.add(board[i][j])
                if board[j][i]!=".":
                    if board[j][i] in valid_col:
                        return False
                    valid_col.add(board[j][i])

                if board[(i//3)*3+j//3][3*(i%3)+j%3]!="." :
                    if board[(i//3)*3+j//3][3*(i%3)+j%3] in valid_sqr:
                        return False
                    valid_sqr.add(board[(i//3)*3+j//3][3*(i%3)+j%3])

        return True

a=[['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
Solution().solveSudoku(a)
print(a)


class Solution:
    # 回溯解法
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()
