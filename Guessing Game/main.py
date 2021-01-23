import random
from game_data import data
from art import logo, vs
from random import randint
from clear import clear

total_items = len(data)
continue_game = True
current_score = 0
random_A = random_B = 0
answer = ''

while(continue_game):
    if(current_score != 0):
            random_A = random_B
            random_B = random.randint(0,total_items - 1)


    while(random_A == random_B):
        random_B = random.randint(0,total_items - 1)

    print(logo)
    if(current_score != 0):
        print(f"You're right! Current score: {current_score}.")

    print(f"Compare A: {data[random_A]['name']}, {data[random_A]['description']}, from {data[random_A]['country']}.")
    print(vs)
    print(f"Against B: {data[random_B]['name']}, {data[random_B]['description']}, from {data[random_B]['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_A = data[random_A]['follower_count']
    followers_B = data[random_B]['follower_count']

    if(answer == 'a' and followers_A > followers_B or answer == 'b' and followers_B > followers_A):
        current_score += 1
    else:
        continue_game = False

print(f"Sorry, that's wrong. Final score: {current_score}.")
