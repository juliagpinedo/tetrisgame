"""
Text interface for the Tetris game.
Controls: A (left), D (right), S (drop), R (rotate), Q (quit)
"""

from tetris_logic import TetrisLogic

def main():
    """
    Starts the Tetris game with a fixed board size and listens for user commands
    """
    rows = 15
    cols = 10
    print(f'Tetris Game Started with {rows} rows and {cols} columns')
    print('Controls: A (left), D (right), S (drop), R (rotate), Q (quit)\n')

    game = TetrisLogic(rows, cols)
    game.spawn_piece()
    game.print_board()

    while True:
        try:
            command = input('Command: ').strip().upper()
        except EOFError:
            break
        if command == 'Q':
            break
        elif command == 'S':
            game.drop_piece()
        elif command == 'A':
            game.move_piece('A')
        elif command == 'D':
            game.move_piece('D')
        elif command == 'R':
            game.rotate_piece()
        game.print_board()

if __name__ == '__main__':
    main()
