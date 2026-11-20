import random
import game_data
import art
from art import logo
from game_data import data
print(logo)
score=0
account_b=random.choice(data)
game_on=True
turns = 3

while turns > 0:
    """User only have 3 chances to play the game"""

    def account_detail(account):
        #Takes the account data and print
        account_name=account["name"]
        account_descr=account["description"]
        account_country=account["country"]
        return f" {account_name} a {account_descr} from {account_country}"

    account_a=account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b=random.choice(data)

    def compare_answer(a_account,b_account,user_guess, a_follower_count,b_follower_count):
        #Take user's guess and the follower counts and returns if they got it right
        if a_follower_count>b_follower_count:
            return user_guess=="a"
        else:
            return user_guess=="b"


    print("Compare A:",account_detail(account_a))
    print(art.vs)
    print("Against B:",account_detail(account_b))
    guess=input("Who has more followers? Type A or B:").lower()
    account_count_a=account_a["follower_count"]
    account_count_b=account_b["follower_count"]

    is_answer_correct=compare_answer(account_a,account_b,guess,account_count_a,account_count_b)


    if is_answer_correct:
        score += 1
        print(f"Correct! Your score is: {score}")
    else:
        print("Incorrect answer!")

    turns -= 1

print(f"Game Over! Final score: {score}/3")