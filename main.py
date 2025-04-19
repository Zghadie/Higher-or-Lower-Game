# import random
# import art
# import game_data
# print(art.logo)
#
#
# choice1 = random.choice(list(game_data.data))
# print(choice1)
# print(art.vs)
# choice2 = random.choice(list(game_data.data))
# print(choice2)

#display art
from art import logo, vs
from game_data import data
import random

def formate_data(account):
    """takes the account data and returns the printable format"""
    account_name = account["name"]
    account_discr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_discr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """take the users guess and the follower count and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess =="a"
    else:
        return  user_guess == "b"
print(logo)
#score keeping
score = 0
game_should_continue = True
account_b = random.choice(data)
#make the game repeatable
while game_should_continue:
    #generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A:{formate_data(account_a)}.")
    print(vs)
    print(f"Against B:{formate_data(account_b)}.")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
    print("\n" * 15)
    print(logo)
    #check if user is correct
    ## get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## get follower count of each account
    ##use if statement to check if user is correct

    #give user feedback on their guess
    #score keeping
    if is_correct:
        score += 1
        print(f"You're right! current score {score}")
    else:
        print(f"sorry, that's wrong your score is {score}")
        game_should_continue = False





#make accounts at position B become at position A