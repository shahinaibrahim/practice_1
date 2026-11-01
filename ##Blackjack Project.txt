##Blackjack Project

import random

def Game_on_off():

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card= random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_score(u_score, c_score):
        if c_score==u_score:
            return "draw"
        elif c_score==0:
            return "You lose,computer has a blackjack"
        elif u_score==0:
            return "You win"
        elif c_score>21:
            return "Computer went over,You win!"
        elif u_score>21:
            return "you went over, you lose!"
        elif u_score>c_score:
            return "You win!"
        else:
            return " you lose"




    your_card = []
    computer_card = []
    computer_score = -1
    your_score = -1

    for _ in range(2):
        your_card.append(deal_card())
        computer_card.append(deal_card())



    is_game_over = False


    while not is_game_over:
        your_score = calculate_score(your_card)
        computer_score = calculate_score(computer_card)

        print(f"Your card is:{your_card}\ncurrent score is:{your_score}")
        print(f"Computer first card is:{computer_card[0]}")

        if your_score==0 and computer_score==0 or your_score>21:
            is_game_over=True

        else:
            new_draw=input("Do you want to draw another card? type 'y' to draw or 'p' to pass:").lower()

            if new_draw=="y":
                your_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score>17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand: {your_card}, your final score: {your_score}")
    print(f"Computer's final hand: {computer_card}, computer final score: {computer_score}")
    print(compare_score(your_score, computer_score))

while input("Do you want to play a game of blackjack? type 'y' to play or 'n' to exit:").lower() == "y":
    Game_on_off()


