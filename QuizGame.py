#Prompt the user to enter a name
#Prompt the user to select an input to proceed with the quiz
#Using the selection statement, ask the user questions and then print result if user input is correct or false

name = input("Enter your name")

print(f"Welcome {name} to your quiz game")
welcome_prompt = int(input("Press 1 to Start"))

if welcome_prompt == 1:
    question_1 = input("Question 1: When did Nigeria get her Independence?")
    if question_1 == "1960":
        print("Correct!")
    else:
        print("Failed")
    question_2 = input("Question 2: What does BBC stand for?")
    if question_2 == "British Broadcasting Corporation":
        print("Correct!")
    else:
        print("Failed")
    question_3 = input("How many days are in a leap year?")
    if question_3 == "366":
        print("Correct!")
    else:
        print("Failed")
    question_4 = input("In meters, how long is an Olympic swimming pool?")
    if question_4 == "50 metres":
        print("Correct!")
    else:
        print("Failed")
else:
    print("Your quiz has ended")
