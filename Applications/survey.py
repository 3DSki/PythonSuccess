
'''
This script is an example af a survey processor.
It process a list of tuples that describe survey questions.
Each tuple contains the category, the question, and a reference to a validator callback.
'''

def validate_range(user_input):
    '''
    This validator is look for 1, 2, 3, 4, 5,or x.
    The user's response is returned, else False
    '''
    # input can be 1 to 5, or "x" to exit...
    if len(user_input) == 1 and "12345x".find(user_input) != -1:
        return user_input
    else:
        return False
        
def evaluate_answer(question, validator_callback):
    '''
    Get's the user's input using question and evalates the response using validator_callback.
    It will continue to loop for valid input.
    '''
    invalid = True
    while invalid:
        answer = input(question)
        answer = validator_callback(answer)
        if answer == False:
            print("Please respond with digits 1 to 5, or x to exit")
        else:
            return answer

def process_survey(questionaire):
    '''
    Processes a list of question tuples with the format category, question, validator callback.
    '''
    survey = {}    
    for question in questionaire:
        response = evaluate_answer(question[1], question[2])
        if response == 'x':
            break
        else:
            survey[question[0]]=response
    return survey    


# ----------------------------------------------------------------------------
# Question Dictionaries
# Each tuple has the category, question, and a validator handler for the user input
question_1 = ("Price", "How would you rate the price?", validate_range)
question_2 = ("Ease", "How would you rate the ease of use?", validate_range)
question_3 = ("Recommendation", "How likely would recomment it to a friend?", validate_range)

# Survey Dictionary
survey = [question_1, question_2, question_3]
# -----------------------------------------------------------------------------
print('Please rate each of the following on a scale from 1 to 5.')

# Pass the list of question tuples to process_survey()
results = process_survey(survey)
for key, value in results.items():
    print( f"{key} {value}")
