############### Blackjack Project #####################
import random
from operations import check_house, random_number, check_sum, score

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
house = []
player = []
player_busted = False
house_busted = False
player_score = house_score = 0
play_hand = 'y'
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# Initial draw
def initial_draw():
    for n in range(0,3):
        if(n == 0 or n == 1):
            random_index = random.randint(0,len(cards) - 1)
            player.append(cards[random_index])
        else:
            random_index = random.randint(0,len(cards) - 1)
            house.append(cards[random_index])
    print(check_sum(player))


# Implement the append for the house. If the sum reachhes 17 or over, stop. Finally, compare
# the house sum with the player sum

while(play_hand == 'y'):
    initial_draw()
    play_another_round = input("Do you want to draw a card (y/n)?\n")
    
    while(play_another_round == 'y'):
        sum = random_number(cards, player)[0]
        if(sum > 21):
            print("Busted!")
            player_busted = True
            
        if(player_busted == True):
            play_another_round = 'n'
        else:
            play_another_round = input("Do you want to draw another card (y/n)?")
    
    print(f"House busted? {house_busted}")
    check_house(player_busted, cards, house, house_busted)
    house_busted = check_house(player_busted, cards, house, house_busted)[1]
    print(f"House busted? {house_busted}")
    
    sum_player = check_sum(player)
    sum_house = check_sum(house)
    print(f"Player sum: {sum_player}\nHouse sum: {sum_house}")

    
    [player_score, house_score] = score(house_score, player_score, player_busted, house_busted, house, player)
    print(f"Your score: {player_score}\nHouse score: {house_score}\n")


    player = []
    house = []
    player_busted = False
    house_busted = False
    play_hand = input("Do you want to play again (y/n)?\n")

print("Thanks for playing Blackjack! See you again soon.")