"""
Game logic module for a Tetris game.
Handles piece movement, rotation, locking, and line clearing
"""

import random
from typing import List, Tuple, Optional

# Tetromino definitions (shapes in grid format)
TETROMINOS = {
    'I': [[' ', ' ', ' ', ' '],
          ['X', 'X', 'X', 'X'],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ']],
    'O': [['X', 'X'],
          ['X', 'X']],
    'T': [[' ', 'X', ' '],
          ['X', 'X', 'X'],
          [' ', ' ', ' ']],
    'L': [['X', ' ', ' '],
          ['X', 'X', 'X'],
          [' ', ' ', ' ']],
    'J': [[' ', ' ', 'X'],
          ['X', 'X', 'X'],
          [' ', ' ', ' ']],
    'S': [[' ', 'X', 'X'],
          ['X', 'X', ' '],
          [' ', ' ', ' ']],
    'Z': [['X', 'X', ' '],
          [' ', 'X', 'X'],
          [' ', ' ', ' ']]
}

class TetrisLogic:
    def __init__(self, rows: int, cols: int):
        """
        Initializes the Tetris game board and game state

        Args:
            rows (int): Number of rows in the game board
            cols (int): Number of columns in the game board

        Returns:
            None
        """
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_piece: Optional[List[List[str]]] = None
        self.piece_position: Tuple[int, int] = (0, 0)

    def spawn_piece(self):
        """
        Randomly selects a tetromino and spawns it at the top center of the board

        Returns:
            None
        """
        piece_type = random.choice(list(TETROMINOS.keys()))
        self.current_piece = [row[:] for row in TETROMINOS[piece_type]]
        start_col = self.cols // 2 - len(self.current_piece[0]) // 2
        self.piece_position = (0, start_col)

    def rotate_piece(self):
        """
        Rotates the current piece 90 degrees clockwise

        Returns:
            None
        """
        if not self.current_piece:
            return
        self.current_piece = [list(row) for row in zip(*self.current_piece[::-1])]

    def move_piece(self, direction: str):
        """
        Moves the piece left or right based on the direction

        Args:
            direction (str): Direction of movement, 'A' = left, 'D' = right
        
        Returns:
            None
        """
        row, col = self.piece_position
        if direction == 'A' and col > 0:
            self.piece_position = (row, col - 1)
        elif direction == 'D' and col + len(self.current_piece[0]) < self.cols:
            self.piece_position = (row, col + 1)

    def drop_piece(self):
        """
        Moves the piece one row down. If it cannot move, locks it and spawns a new piece

        Returns:
            None
        """
        row, col = self.piece_position
        if self.can_move_down():
            self.piece_position = (row + 1, col)
        else:
            self.lock_piece()
            self.clear_lines()
            self.spawn_piece()

    def can_move_down(self) -> bool:
        """
        Checks if the piece can be dropped one row without collision or going out of bounds

        Returns:
            bool: True if the piece can move down, False otherwise
        """
        if not self.current_piece:
            return False
        row, col = self.piece_position
        for i, piece_row in enumerate(self.current_piece):
            for j, cell in enumerate(piece_row):
                if cell == 'X':
                    new_row = row + i + 1
                    if new_row >= self.rows or self.board[new_row][col + j] == 'X':
                        return False
        return True

    def lock_piece(self):
        """
        Adds the current piece to the board, turning it into static blocks

        Returns:
            None
        """
        row, col = self.piece_position
        for i, piece_row in enumerate(self.current_piece):
            for j, cell in enumerate(piece_row):
                if cell == 'X':
                    self.board[row + i][col + j] = 'X'
        self.current_piece = None

    def clear_lines(self):
        """
        Clears any full lines from the board and shifts the remaining lines downward

        Returns:
            None
        """
        self.board = [row for row in self.board if any(cell == ' ' for cell in row)]
        while len(self.board) < self.rows:
            self.board.insert(0, [' ' for _ in range(self.cols)])

    def print_board(self):
        """
        Prints the current game board, including the falling piece

        Returns:
            None
        """
        temp_board = [row[:] for row in self.board]
        if self.current_piece:
            row, col = self.piece_position
            for i, piece_row in enumerate(self.current_piece):
                for j, cell in enumerate(piece_row):
                    if cell == 'X':
                        board_row = row + i
                        board_col = col + j
                        if 0 <= board_row < self.rows and 0 <= board_col < self.cols:
                            temp_board[board_row][board_col] = 'X'
        for row in temp_board:
            print('|' + ''.join(row) + '|')
        print(' ' + '-' * self.cols)
