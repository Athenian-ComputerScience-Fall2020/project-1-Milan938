# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  None so far
import random

def pres_info(president):
    print("You will be given a hint and a guess. If you guess wrong, you get another hint and guess. ", 
    "You will keep getting hints and guesses until you have guessed 5 times.")
    print(president[0])
    print("Which president do you think this is?: ")
    answer = input()
    if answer == president[6]:
        print("Congratulations, that was the right answer!")
    elif answer != president[6]:
        print(president[5])
        print(president[1])
        print("Which president do you think this is?: ")
        answer2 = input()
        if answer2 == president[6]:
            print("Congratulations, that was the right answer!")
        elif answer2 != president[6]:
            print(president[5])
            print(president[2])
            print("Which president do you think this is?: ")
            answer3 = input()
            if answer3 == president[6]:
                print("Congratulations, that was the right answer!")
            elif answer3 != president[6]:
                print(president[5])
                print(president[3])
                print("Which president do you think this is?: ")
                answer4 = input()
                if answer4 == president[6]:
                    print("Which president do you think this is?: ")
                elif answer4 != president[6]:
                    print(president[5])
                    print(president[4])
                    print("Which president do you. think this is?: ")
                    answer5 = input()
                    if answer5 == president[6]:
                        print("Congratulations, that was the right answer!")
                    elif answer5 != president[6]:
                        print("I'm sorry, you're out of guesses")


choice = random.randint(1, 4)

taft = ["This president was the first president to throw the first pitch of the baseball season",
"This president got stuck in a bath tub and needed six men to help get him out", "This man remains the heaviest president ever, at 330 pounds",
"This man was the first president to be buried at Arlington", "This man was the only president who also served on the supreme court",
"I'm sorry, please guess again", "William Taft"]

obama = ["He was the first African American president ever elected", "His VP was Joe Biden", 
    "He was a senator from Illinois before becoming president", "He was born in Honolulu", 
    "He was elected to two terms as president", "Wrong answer, please guess again", "Barack Obama"]

lincoln = ["This former president was born on February 12, 1809", "This man was president for 4 years", 
"He was one of four presidents ever assasinated", "He was the tallest president ever elected",
"This man was known for his tophat and beard", "Wrong answer, please guess again", "Abraham Lincoln"]

teddy = ["This man remains the youngest president who took office", "He became president after William McKinley was assasinated",
"He was shot before a campaign speech in Milwaukee", "He remains the only president to serve more than two terms",
"His nickname the name for a stuffed bear", "I'm sorry, that wasn't right, please guess again",
"Teddy Roosevelt"]

if choice == 1:
    pres_info(obama)

if choice == 2:
    pres_info(lincoln)

if choice == 3:
    pres_info(teddy)

if choice == 4:
    pres_info(taft)

