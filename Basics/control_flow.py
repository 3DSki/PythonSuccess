'''
if-elif-else, for, and while, continue, break
match-case as a variation to if-elif-else, or switch-case in other lanuguages
'''
current_value = 10
msg = ''

# It's manditory that you indent the instructions under each if/elfi/else expression!!!
if current_value == 10:
    msg = 'Perfect!'
elif current_value < 10 and current_value > 5:  # example were 2 conditions must be met (use of and)
    msg = 'Try just a bit more.'
else:    # instructions under else become the default result no other conditions are met.
    msg = 'No rating available at this time'   

print(msg)

# Reimplementation of the above for reuse via a function definition
# It's manditory that the instruction in a function are indented, and all 
# other required indentions occur within that!!!
def evaluate(value):
    if value == 10:
        msg = 'Perfect!'
    elif value < 10 and value > 5:  # example were 2 conditions must be met (use of and)
        msg = 'Try just a bit more.'
    else:    # instructions under else become the default result no other conditions are met.
        msg = 'No rating available at this time'   

    return msg

current_value = 7
print(evaluate(current_value))
current_value = 4
print(evaluate(current_value))

# Evaluating each item in a list using a for loop and a call to our evaluate() function
# for-in will automatically end when there are no more items to evaluate from the list
different_ratings = [1,3,4,2,5,7,10,9]
for current_value in different_ratings:
    print("Score: " + str(current_value) + " " + evaluate(current_value))

# OUTPUT...
# Score: 1 No rating available at this time
# Score: 3 No rating available at this time
# Score: 4 No rating available at this time
# Score: 2 No rating available at this time
# Score: 5 No rating available at this time
# Score: 7 Try just a bit more.
# Score: 10 Perfect!
# Score: 9 Try just a bit more.

# Using match-case to test patterns/values.
# This is a reimplemention of our earlier evaluate() function.
def evaluate2(value):
    match value:
        case 10:
            msg = 'Perfect!'
        case 6|7|8|9:       # using value with "or" (|)  value < 10 and value > 5
            msg = 'Try just a bit more.'
        case _:
            msg = 'No rating available at this time'   

    return msg

different_ratings = [1,3,4,2,5,7,10,9]
for current_value in different_ratings:
    print("Score: " + str(current_value) + " " + evaluate2(current_value))

# In the definitions of evaluate() and evaluate2() we would say that we are using a "single point of return".
# This is because msg can be assigned a value at multiple points, but not returned until the bottom. This
# practice is usually prefered, but here is a different implmentation where there are multiple return points.
def evaluate3(value):
    match value:
        case 10:
            return 'Perfect!'
        case 6|7|8|9:       # using value with "or" (|)  value < 10 and value > 5
            return 'Try just a bit more.'
        case _:
            return 'No rating available at this time'   

for current_value in different_ratings:
    print("Score: " + str(current_value) + " " + evaluate3(current_value))  # evaluation3() called

# Notice that there are different approaches to doing things. Programming is a matter of following
# best practices and evaluating efficiency in larger applications. 

# Finding a tuple in a list of tuples
my_location = (6,4)
locations = [(0,5), (3,2), (6,4), (7,1)]
for location in locations:
    if my_location == location:
        print("Found you at " + str(location))
# OUTPUT:
# Found you at (6, 4)

# using index to locate the tuple
# Remember that my_location is still (6,4)
found = locations.index(my_location)
if -1 != found:
    print("You are at " + str(locations[found]))
else:
    print("You're not at any of our locations.")
# OUTPUT:
# You are at (6, 4)

# While is more often used as a main application loop, to keep it running until the user exits
# Remember to indent your code blocks!!!
running = True
while running:
    state = input("R to run, or anything else to quit.")
    if 'R' != state:
        running = False

print("Done!")
# Output...
# R to run, or anything else to quit.R
# R to run, or anything else to quit.a
# Done!

