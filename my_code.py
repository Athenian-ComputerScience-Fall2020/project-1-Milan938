# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  None so far

def pres_info(hint_1, hint_2, hint_3, hint_4, hint_5, error_message, right_answer):
    print("You will be given a hint and a guess. If you guess wrong, you get another hint and guess. ", 
    "You will keep getting hints and guesses until you have guessed 5 times.")
    print(hint_1)
    print("Which president do you think this is?: ")
    answer = input()
    if answer != right_answer:
        print(error_message)
        print(hint_2)
        print("Which president do you think this is?: ")
        answer2 = input()
    elif answer == right_answer:
        print("Congratulations, that was the right answer!")
    if answer2 != right_answer:
        print(error_message)
        print(hint_3)
        print("Which president do you think this is?: ")
        answer3 = input()
    elif answer2 == right_answer:
        print("Congratulations, that was the right answer!")
    if answer3 != right_answer:
        print(error_message)
        print(hint_4)
        print("Which president do you think this is?: ")
        answer4 = input()
    elif answer3 == right_answer:
        print("Congratulations, that was the right answer!")
    if answer4 != right_answer:
        print(error_message)
        print(hint_5)
        print("Which president do you. think this is?: ")
        answer5 = input()
    elif answer4 == right_answer:
        print("Which president do you. think this is?: ")
    if answer5 != right_answer:
        print("I'm sorry, you're out of guesses")



pres_info("He was black", "He is red", "He likes flowers", "He smells bad", "aaahhhh", "Please guess again", "Obama")