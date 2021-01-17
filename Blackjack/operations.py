import random

def random_number(cards, player):
    random_index = random.randint(0, len(cards) - 1)
    player.append(cards[random_index])
    sum_player = check_sum(player)
    #print(f"Your sum: {sum_player}")
    return [sum_player, player]


def check_sum(list):
    sum = 0
    for list_item in list:
        sum += list_item
    return sum


def check_house(player_busted, cards, house, house_busted):
    if(player_busted == False):
        total_house = check_sum(house)
        while(total_house < 17):
            total_house = random_number(cards, house)[0]

        if(total_house > 21):
            house_busted = True
            print("House busted!")
            return [house, True]
        else:
            return [house, False]

        
        print(f"Total sum of the house: {total_house}")
    else:
        return [house, False]


def score(house_score, player_score, player_busted, house_busted, house, player):
    if(player_busted == False):
        sum_player = check_sum(player)
        sum_house = check_sum(house)
        #print(f"Player sum: {sum_player}\nHouse sum: {sum_house}")
        if(sum_player > sum_house):
            print("You win!")
            player_score += 1
            print(f"Player scores. Score: {player_score}")
            return [player_score, house_score]

        elif(sum_player == sum_house):
            print(f"It's a draw. No one scores.")
            return[player_score, house_score]

        else:
            if(house_busted == False):
                house_score += 1
                print(f"House scores. Score: {house_score}")
                return [player_score, house_score]
            else:
                player_score += 1
                print(f"Player scores. Score: {player_score}")
                return [player_score, house_score]
    else:
            house_score += 1
            print(f"House scores. Score: {house_score}")
            return [player_score, house_score]