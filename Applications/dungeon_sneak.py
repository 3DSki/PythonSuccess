import random

# Define the game world grid as a tuple of tuples
world = (
    ('N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('W', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E'),
    ('S', 'S', 'S', 'S', 'S', 'S', 'L', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S')
)
# Player's initial state
player_position = [0, 0, 'N']  # row, column, orientation

# Function to find a random valid start position within the room
def initialize_player():
    while True:
        row = random.randint(1, 14)
        col = random.randint(1, 14)
        if world[row][col] == '0':
            orientation = random.choice(['N', 'E', 'S', 'W'])
            player_position[0], player_position[1], player_position[2] = row, col, orientation
            break

# Function to display player's position and orientation
def display_position():
    print(f"Player is at row {player_position[0]}, column {player_position[1]}, facing {player_position[2]}.")

# Function to get a valid user input
def get_user_input():
    while True:
        choice = input("Enter a command (w: North, a: West, s: South, d: East, l: Look, x: Exit): ").strip().lower()
        if choice in {'w', 'a', 's', 'd', 'l', 'x'}:
            return choice
        else:
            print("Invalid choice. Please enter 'w', 'a', 's', 'd', 'l', or 'x'.")

# Function to handle movement and game logic
def move_player(direction):
    row, col, _ = player_position

    if direction == 'N':
        row -= 1
    elif direction == 'S':
        row += 1
    elif direction == 'W':
        col -= 1
    elif direction == 'E':
        col += 1

    if 0 <= row < 16 and 0 <= col < 16 and world[row][col] == '0':
        player_position[0], player_position[1] = row, col
    else:
        print("You can't move in that direction.")

# Game loop
def game_loop():
    initialize_player()
    print("Welcome to the Text Adventure Game!")
    while True:
        display_position()
        command = get_user_input()

        if command == 'x':
            print("Exiting the game. Goodbye!")
            break
        elif command == 'l':
            print("You are in a small square room. The east wall has a locked door. You need a key to open it.")
        else:
            if command == 'w':
                player_position[2] = 'N'
            elif command == 'a':
                player_position[2] = 'W'
            elif command == 's':
                player_position[2] = 'S'
            elif command == 'd':
                player_position[2] = 'E'

            # Attempt to move in the direction of the current orientation
            move_player(player_position[2])

# Start the game
game_loop()
