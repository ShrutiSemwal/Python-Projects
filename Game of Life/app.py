"""
The game uses a rectangular grid of cells of infinite size in which each cell is empty or occupied by an organism. 
It is said that occupied cells are alive, while empty ones are dead. 
The game is played over a specific period, with each turn creating a new “generation” based on the arrangement of living organisms in the current configuration.

The status of a cell in the next generation is determined by applying the following four basic rules to each cell of the current configuration:

1.If a cell is alive and has two or three living neighbours, the cell stays alive in the next generation.
2.A living cell that has no living neighbours or only one living neighbour dies of isolation in the next generation.
3.A living cell that has four or more living neighbours dies from overpopulation in the next generation.
4.A dead cell with exactly three living neighbours results in birth and becomes alive in the next generation.
"""

from typing import List

class game_of_life:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


#TEST CODE
def print_board(board):
    for row in board:
        print(" ".join("■" if cell == 1 else "□" for cell in row))
    print()


board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

game = game_of_life()

print("Initial:")
print_board(board)

game.gameOfLife(board)

print("Next Generation:")
print_board(board)