# Tetris Python Game!

This repository implements the Tetris game in Python using a text-based interface. You control the falling pieces using keyboard commands, and the game is displayed directly in the console.

## How to Play?

The game board has a fixed size (15 rows x 10 columns). A random Tetris piece (tetromino) will appear at the top of the board. Your task is to control its movement and fit it into place to complete horizontal lines.

When a horizontal line is filled with blocks, it disappears and you earn space. If a piece reaches the top of the board and cannot spawn, the game will end.

## Executing the Code:

1. Make sure you have Python 3 installed.
2. Place both `tetris_ui.py` and `tetris_logic.py` in the same directory.
3. Run the game:

```bash
python3 tetris_ui.py
```

## Controls:

| Command | Action                      |
|---------|-----------------------------|
| `A`     | Move piece left             |
| `D`     | Move piece right            |
| `S`     | Drop piece one row          |
| `R`     | Rotate piece clockwise      |
| `Q`     | Quit the game               |

## Notes:

- Pieces will automatically "lock" into the board if they can't fall further.
- Full horizontal lines are automatically cleared and rows above drop down.
- New pieces are spawned after the current one locks.

---

