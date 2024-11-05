'''
This is an example of a multi-line comment

'''
import statistics

# Names are in snake-case. Each part is meaningful and separated with an underscore.
cat_count = 3
dog_count = 4
reptile_count = 2

# Addition
animal_count = cat_count + dog_count + reptile_count

# Basic print with f"<string>" formatting
print( f"Total Animals: {animal_count}")

# Multiplication
meal_count = 3
days_in_week = 7
meals_per_wk = meal_count * days_in_week

# Print using the string.formt() method, with positional placeholder(s).
print("Meals Per Week: {0}".format(meals_per_wk))

# Division
allowance = 40
allowance_per_day = allowance / days_in_week

# Using type() to show the type of allowance_per_day:  <class 'float'>
print(type(allowance_per_day))
# Print with decimal formatting to 2 decimal places.
print("Allowance Per Day: {0:.2f}".format(allowance_per_day))

# Operator Precedence: Multiplication before addition
answer =  cat_count + meal_count * days_in_week
print( "Default Precedence (multiplication first): " + str(answer)) # 24
# ... Change Precedence with grouping parentheses
answer =  (cat_count + meal_count) * days_in_week
# Note use of str() to convert the numeric 42 to a string for concatenation.
print( "Grouping same computation to perform addition first: " + str(answer)) # 42

# Modulus
remainder = days_in_week % meal_count
print( "Modulus: "+ str(remainder))

# Conversion from string to int
# String integer
int_string = "42"
print( type(int_string))        # using type() to determine the type of a variable
string_to_int = int(int_string)
print( type(string_to_int))     # using type() to determine the type of a variable

# Attempting to add an int to a str will fail
# int_string + string_to_int

# The += Operator
num = 2
print("num is " + str(num))
num+=3
print("num+=3: "+ str(num))

# The -= Operator
print("num is " + str(num))
num-=3
print("num-=3: "+ str(num))

# The *= Operator
print("num is " + str(num))
num*=3
print("num*=3: "+ str(num))

# The /= Operator
print("num is " + str(num))
num/=3
print("num/=3: "+ str(num))

# The %= Operator
num = 7
print("num is " + str(num))
num%=2
print("num%=2: "+ str(num))

# A list of str (strings)
animals = ["dog", "cat", "alegator"]
print(animals)
animals.sort()  # Sort the list in-place
print(animals)
animals.reverse()  # reverse the list in-place
print(animals)
print("removed: "+ animals.pop())
print(animals)
animals.append("garilla")
print(animals)

# List of integers
grades = [100, 75, 55, 62, 87, 79]
print(grades)
grades.sort() # sorted in-place
print(grades) # [55, 62, 75, 79, 87, 100]
grades.reverse() # reversed in-place
print(grades) # [100, 87, 79, 75, 62, 55]
# Notice slice syntax!!!
print(grades[1:3]) #  slice is [87, 79]

# Use statistics.mean() to find the average grade from grades
print(statistics.mean(grades))

# Built-in sum() to sum grades
print(sum(grades))

# SPECIAL: NOT MENTIONED IN THE BOOK!!!
# SETS (notice the curly braces that wrap the list)
grades_1 = {100, 75, 55, 62, 87, 79}
grades_2 = {99, 74, 55, 62, 88, 80}

# the intersection of the sets (shared items)
shared = grades_1.intersection(grades_2)  # {62,55}
print(shared)
# Shorthand for intersection: &
shared = grades_1 & grades_2  # {62,55}
print(shared)

# the difference of the sets (shared items)
diff = grades_1.difference(grades_2)  # {75, 100, 79, 87}
print(diff)
# Shorthand for difference: -
diff = grades_1 - grades_2  # {75, 100, 79, 87}
print(diff)
