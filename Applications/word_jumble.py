import random
import string

'''
This code was created in cooperation with ChatGPT. The implementation was described iteratively to reach the
desired specification. Once that was complete, I asked ChatGPT to provided a more optimized version and it
changed the grid be a dictionary of tuple-letter pairs.
 '''
# Define grid size and initialize the grid with random uppercase letters
grid_size = 20
grid = {(row, col): random.choice(string.ascii_uppercase) for row in range(grid_size) for col in range(grid_size)}

# Define the word list with uppercase characters
work_list_of_words = [
    "GUITAR", "PIANO", "VIOLIN", "FLUTE", "SAXOPHONE", 
    "TRUMPET", "DRUMS", "CELLO", "CLARINET", "HARP", 
    "TROMBONE", "BASS"
]

# Initialize the word dictionary
word_properties = {word: {"placed": False, "direction": None, "reversed": None, "placement": []} 
                   for word in work_list_of_words}

# Directions as (row_step, col_step) tuples
DIRECTIONS = {
    "horizontal": (0, 1),
    "vertical": (1, 0),
    "diagonal_ltr": (1, 1),
    "diagonal_rtl": (1, -1)
}

# Track occupied positions
occupied_positions = set()

# Function to check placement conflicts
def check_conflicts(placement):
    for pos in placement:
        if pos in occupied_positions:
            return True
    return False

# Function to plan word placement
def plan_word_placement(word):
    word_length = len(word)
    max_attempts = 100
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        
        # Randomly choose a direction and reversal
        direction, (row_step, col_step) = random.choice(list(DIRECTIONS.items()))
        reversed_word = random.choice([True, False])
        word_to_place = word[::-1] if reversed_word else word

        # Determine starting position
        start_row = random.randint(0, grid_size - 1)
        start_col = random.randint(0, grid_size - 1)

        # Calculate placement positions
        placement = []
        for i, char in enumerate(word_to_place):
            row = start_row + i * row_step
            col = start_col + i * col_step

            # Check boundaries
            if not (0 <= row < grid_size and 0 <= col < grid_size):
                break
            placement.append(((row, col), char))

        # Validate placement
        if len(placement) == word_length and not check_conflicts([pos for pos, _ in placement]):
            return {
                "placed": True,
                "direction": direction,
                "reversed": reversed_word,
                "placement": placement
            }
    
    # Return None if placement fails
    return None

# Function to update the grid with final word placements
def update_grid():
    for word, properties in word_properties.items():
        if properties["placed"]:
            for (row, col), char in properties["placement"]:
                grid[(row, col)] = char
                occupied_positions.add((row, col))

# Place all words
failed_words = []
for word in work_list_of_words:
    placement_data = plan_word_placement(word)
    if placement_data:
        word_properties[word].update(placement_data)
    else:
        failed_words.append(word)

'''
DEBUG PURPOSES...

print("\nWord Properties:")
for word, properties in word_properties.items():
    print(f"{word}: {properties}")
'''
# Print error message if words could not be placed
if failed_words:
    print("\nError: The following words could not be placed in the grid:")
    print(", ".join(failed_words))
else:
    # Update the grid with the final placements
    update_grid()

    # Print the grid
    for row in range(grid_size):
        print("  ".join(grid[(row, col)] for col in range(grid_size)))
        
    # Print the words to search for
    print("\nWords to search for:")
    print(", ".join(work_list_of_words))
