from random import choice
from fast_token_value import chaos_bag_for_pulling, keys_dict


result = 0
chaos_bag = chaos_bag_for_pulling(keys_dict, 'The Labyrinths of Lunasy standard group C', 'Roland Banks')
a = input(f'press "enter" if  is ready to reveal a chaos token')
bag_for_reveal = []
bag_for_reveal.extend(chaos_bag)
reveal_flag = True
token_value = 0
tokens = []
while reveal_flag == True:
        token = choice(bag_for_reveal)
        token_name = f'"{token[0]}"'
        pull_token_value = token[1] if type(token[1]) == int else token[1][0]
        tokens.append(token_name)
        token_value += pull_token_value
        if type(token[1]) != int:
            bag_for_reveal.remove(token)
            print(f'{token[0]} is pulled. Value is {token[1][0]}. You must reveal another token')
        else: 
            reveal_flag = False
            tokens_in_str = ', '.join(tokens)
            is_plural = 'are' if len(tokens) > 1 else 'is'
            last_result = result + token_value
print(f'{tokens_in_str} {is_plural} pulled. Value is {token_value}. Result is {last_result}')
# if (last_result) >= 0:
#     print(N_in_C(player) + text_in_color(f' succeed the skill test by {last_result}', 'green'))
# else: print(N_in_C(player) + text_in_color(f' failed the skill test by {last_result}', 'red'))