from game_data.fast_token_value import keys_dict, chaos_bag_for_pulling
from game_data.prob_funcs import probability_of_list
from random import choice

result = [-2, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]

bag = chaos_bag_for_pulling(keys_dict, 'The Labirinths of Lunasy standard group A', 'Stella Clark')
divider = len(bag)
i = 0
revealed = []
while i < len(bag):
    if type(bag[i][1]) == tuple:
        revealed.append(bag[i][1][0])
        bag.remove(bag[i])
        divider *= len(bag)-1
        i = 0
    else: i += 1

mod1 = sum(revealed)
bag = [i[1]+mod1 for i in bag]
all_prob = 0
x = 1000

for i in range(x):
#    mod = choice(result)
    mod = +200
    print(f'result {mod}')
    probability = probability_of_list(mod, bag)
    probability = probability/(divider/len(bag))
    all_prob += probability

print(all_prob/x * 100)


