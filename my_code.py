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
        print("Which president do you think this is?: ")
    if answer5 != right_answer:
        print("I'm sorry, you're out of guesses")
    elif answer5 == right_answer:
        print("Congratulations, that was the right answer!")


pres_info("He was the first African American president ever elected", "His VP was Joe Biden", 
"He was a senator from Illinois before becoming president", "He was born in Honolulu", 
"He was elected to two terms as president", "Wrong answer, please guess again", "Barack Obama")

pres_info("This former president was born on February 12, 1809", "This man was president for 4 years", 
"He was one of four presidents ever assasinated", "He was the tallest president ever elected",
"This man was known for his tophat and beard", "Wrong answer, please guess again", "Abraham Lincoln")