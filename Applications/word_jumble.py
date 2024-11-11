import random
import string

'''
This is an example implementation of a word jumble puzzle.
'''
def create_empty_puzzle_area(height, width):
    '''
    Creates an N by N grid and fills it with blanks (' ')
    '''
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for h in range(height):
        for w in range(width):
            grid[h][w] = ' '

    return grid


def fill_area_random_letters(area):
    '''
    Fills N by N area with random uppercase characters.
    '''
    for h in range(len(area)):
        for w in range(len(area[0])):
            area[h][w] = random.choice(string.ascii_uppercase)
    return area


def pretty_print_area(area):
    '''
    Utility function used to print the puzzle grid.

    EXAMPLE:

    D  I  Z  F  Q  A  C  B  Z  F  S  E  B  H  X  S  A  W  S  A  
    G  X  E  O  A  X  G  T  Q  Y  I  E  X  H  X  V  E  S  I  P
    L  O  G  O  D  J  M  O  C  V  O  H  X  S  K  G  V  R  J  O
    V  S  S  E  Z  Q  U  J  N  B  A  R  R  U  S  S  X  F  E  E
    X  Q  M  B  S  B  E  Z  U  O  A  A  G  P  I  F  D  U  M  V
    Z  F  B  M  B  T  W  T  W  A  U  M  A  A  Y  T  M  B  I  Z
    E  D  H  S  S  V  C  R  X  U  U  K  L  H  P  K  R  Q  G  Q
    T  M  O  K  Z  K  B  S  Q  Q  O  Y  F  M  C  G  V  Y  F  V
    E  R  L  G  U  R  F  J  L  T  V  K  F  K  Y  R  L  U  Q  G
    U  Z  L  X  V  E  B  B  A  A  O  O  G  M  T  P  R  O  T  P
    R  D  M  K  F  D  K  S  O  X  G  P  I  C  I  P  N  Y  N  D
    Y  C  X  H  R  R  I  Y  A  O  A  J  H  U  Q  X  S  D  P  W
    R  C  X  H  Y  K  U  Y  Z  V  A  N  G  S  C  A  N  J  R  U
    P  X  P  B  Z  D  N  G  S  S  J  Z  V  T  S  P  L  M  X  C
    E  V  D  V  B  G  K  D  V  B  D  B  V  Z  P  U  F  A  J  V
    A  K  X  J  B  A  I  B  J  Y  M  J  Z  Y  W  V  R  J  X  D
    R  L  F  F  L  X  M  C  L  I  W  E  D  D  K  I  W  G  Q  D
    L  X  V  A  E  X  T  Y  F  L  B  M  A  A  Y  F  N  Z  C  C
    I  T  P  A  X  B  K  V  Z  M  Q  M  C  F  I  W  T  Y  C  Z
    K  B  M  V  Q  R  K  C  O  Z  Q  H  Y  G  I  U  Y  N  H  L

    '''
    row = ""
    for h in range(len(area)):
        for w in range(len(area[0])):
            row += (area[h][w] + "  ")
        print(row)
        row=""


def initialize_word_placement_data(words):
    '''
    Takes a list of words and returns a data struct constructed as follows:

    word: {horizontal: True/False, 
           reversed: True/False, 
           placement: [
                {char: [character], row: [grid row], col" [grid column]},
                       ...
           ]
    }

    '''
    words_map = {}
    for word in words:
        words_map[word] = {}
        words_map[word]["placed"] = False
        words_map[word]["horzontal"] = random.choice([True,False])
        words_map[word]["reversed"] = random.choice([True,False])
        words_map[word]["placement"] = []
        char_count = 0
        for char in word:
            words_map[word]["placement"].append({})
            words_map[word]["placement"][char_count]["char"] = char 
            words_map[word]["placement"][char_count]["row"] = 0 
            words_map[word]["placement"][char_count]["col"] = 0 
            char_count+=1
    return words_map

    
# Example list of words ----------------------------:
work_list_of_words = [
"Guitar",
"Piano",
"Violin",
"Flute",
"Saxophone",
"Trumpet",
"Drums",
"Cello",
"Clarinet",
"Harp",
"Trombone",
"Bass"]

# Create and fill the puzzle ares with letters --------------------------------------------------
# Declare a 20x20 array to contain the word jumble.
puzzle_area = create_empty_puzzle_area(20, 20)
puzzle_area = fill_area_random_letters(puzzle_area)
# pretty_print_area(puzzle_area)
# ----------------------------------------------------------------------------------------------
 
# Word Grid Placement Requirements:
#
#   1) Words will only be vertical or horizontal.
#   2) Words will be regular or in reverse.
# ---------------------------------------------------------------------------------------------------------- 
# I've chosen to find the longest words to place them on the grid first, since there's a less chance of shorter words
# colliding with them, or perhaps reducing the collisions only once or twice. We do want some of these word intersections,
# but this is an example and I don't want it to be more complicated than it could be. Here are my construction

# Reverse sort the input list by length...
reversed_by_length = sorted(work_list_of_words, key=len, reverse=True)

# Now some complexity begins. We need to organize all the data regarding the words keep track of how they're place,
# as well as their letter placements on the grid so word intersections can be managed. Class usage is not being
# studied here, so we will other data organization features.
#
# Dictionary, with each word being the key...
#   word: {horizontal: True/False, 
#          reversed: True/False, 
#          placement: [
#               {char: [character], row: [grid row], col" [grid column]},
#                      ...
#          ]
#   }
# ------------------------------------------------------------------------------------------------------------
word_placement_data = initialize_word_placement_data(reversed_by_length)

print(word_placement_data["Saxophone"])

