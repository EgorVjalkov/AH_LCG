from game_data.scenario_token_value import *
from random import choice
# не заклнчил с -99 жетоном!!!!

#skill = int(input('Investigator`s skill = '))
#check = int(input('skill check = '))
chaos_bag = night_of_the_zealot_normal()

def Jacquilyne_Fine_special():
#    result = skill - check
    first = choice(chaos_bag)
    chaos_bag.remove(first)
    second = choice(chaos_bag)
    chaos_bag.remove(second)
    third = choice(chaos_bag)
    chaos_bag.remove(third)
    tokens = [first, second, third]
    print(f'Tokens are {tokens}.' )
    if not -99 in tokens:
        choosed = int(input('What token do you choose? press "1", "2" or "3": ' ))
        return tokens[choosed-1]
    else: 
        tokens = [i for i in tokens if not -99]
        print(tokens)
        return tokens[0] + tokens[1]

print(Jacquilyne_Fine_special())