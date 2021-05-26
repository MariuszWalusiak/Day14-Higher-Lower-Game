# import asciiart from art
import random
from artDay14 import logo, vs
from game_dataDay14 import data
import os


# function which choose random person to compare
def draw_person():
    return random.choice(data)

# Function which compares number of followers


def compare_people(person_A, person_B):
    if person_A["follower_count"] > person_B["follower_count"]:
        return "a"
    else:
        return "b"

# Function Comparing user's answer with correct answer


def compare_answers(user_answer, proper_answer):
    if user_answer == proper_answer:
        """It return True if answer is right  or False if it's wrong  """
        return True  # print("you get point")
    else:
        return False  # print("you gave wrong anwer")

# chose random people to compare


person_A = draw_person()
person_B = draw_person()

should_Continue = True
# set initial user's score
user_score = 0

print(logo)

while should_Continue:

    # print(f"person_A followers{person_A['follower_count']}")
    # print(f"person_B followers{person_B['follower_count']}")

    # Create information lines for user
    print(
        f"Compare A: {(person_A['name'])}, {person_A['description']}, from {person_A['country']}")

    print(vs)
    print(
        f"Against B: {(person_B['name'])}, {person_B['description']}, from {person_B['country']}")

    # user choose which has more follewers
    user_choice = input("Who has more followers? type 'A' or 'B'").lower()
    # compare answers
    result = compare_answers(user_choice, compare_people(person_A, person_B))

    if result == True:
        person_A = person_B
        person_B = draw_person()
        user_score += 1
        os.system('cls')
        print(logo)
        print(f"You are right! Current score: {user_score}")
    else:
        print(user_score)
        should_Continue = False
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {user_score}")
