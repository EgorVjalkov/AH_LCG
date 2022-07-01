from game_data.scenario_token_value import *
from random import choice
#сложности с логикой. Нада учить словари. Придумать последовательность проверки навыка

#skill = int(input('Investigator`s skill = '))
#check = int(input('skill check = '))
chaos_bag = night_of_the_zealot_normal_bag_keys


def Jacquilyne_Fine_special(pull_tokens):
#    result = skill - check
    pull_tokens = pull_tokens + 2
#    print(pull_tokens)
    tokens = []
    for i in range(pull_tokens):
        i = choice(chaos_bag)
        chaos_bag.remove(i)
        tokens.append(i)
    if not 'auto_fail' in tokens:
        for i in range(2):
            print(f'Tokens are {tokens}.' )
            cancelled = int(input(f'What token do you cancelled? press num from "1" to "{pull_tokens-i}": '))
            tokens.remove(tokens[cancelled-1])
        return tokens
    else: 
        tokens = [i for i in tokens if not i == 'auto_fail']
        tokens.remove('auto_fail')
        return tokens

print(Jacquilyne_Fine_special(5))


#    first = choice(chaos_bag)
#    chaos_bag.remove(first)
#    second = choice(chaos_bag)
#    chaos_bag.remove(second)
#    third = choice(chaos_bag)
#    chaos_bag.remove(third)