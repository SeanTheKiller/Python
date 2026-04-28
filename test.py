import os

# 1. The Map (Logic: # is a wall, . is a floor)
tile_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#", ".", "#"],
    ["#", ".", "#", ".", ".", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "E", "#"],
]

# 2. Initial State
player_pos = [1, 1]  # [row, col]

def draw_map():
    os.system('cls' if os.name == 'nt' else 'clear') # Refresh screen
    for r, row in enumerate(tile_map):
        row_str = ""
        for c, tile in enumerate(row):
            if [r, c] == player_pos:
                row_str += "@ " # The Player
            else:
                row_str += tile + " "
        print(row_str)

# 3. Movement Logic Loop
while True:
    draw_map()
    move = input("Move (WASD): ").lower()

    # Calculate "Potential" new position
    new_row, new_col = player_pos[0], player_pos[1]

    if move == "w": new_row -= 1
    elif move == "s": new_row += 1
    elif move == "a": new_col -= 1
    elif move == "d": new_col += 1
    elif move == "q": break

    # The Logic Gate: Check if the move is valid
       # The Logic Gate: Check if the move is valid
    if tile_map[new_row][new_col] == ".":
        player_pos = [new_row, new_col]
    elif tile_map[new_row][new_col] == "#":
        print("\nOuch! You hit a wall.")
        input("Press Enter to continue...")
    elif tile_map[new_row][new_col] == "E":
        print("\nCongratulations! You found the exit!")
        break


