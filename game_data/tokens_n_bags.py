from funcs.input_checking import input_checking as ICh # like a module
from funcs.colored_keywords import names_in_color as N_in_C # like a module
from game_data.fast_token_value import Elder_Sign


# The Night of a Zealot scenarios

The_Night_of_Zealot_standard_bag = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign']

The_Gathering_standard_symbols = {
    'skull': {
        'value': '"skull": what is the number of Ghoul enemies at your location? Press a "num" and "enter" '},
    'cultist': {
        'value': -1,
        'fail': 'take 1 horror'},
    'tablet': {
        'value': -2,
        'instant effect': 'take 1 damage'}
}

The_Midnight_Masks_standard_symbols = {
    'skull': {
        'value': '"skull": what is the highest number of doom on a Cultist enemy in play? Press a "num" and "enter" '},
    'cultist': {
        'value': -2,
        'instant effect': 'place 1 doom on the nearest Cultist enemy'},
    'tablet': {
        'value': -3,
        'fail': 'place 1 of your clues on your location'}
}

The_Devourer_Below_standard_bag = The_Night_of_Zealot_standard_bag.copy()
The_Devourer_Below_standard_bag.append('Elder Thing')

The_Devourer_Below_standard_symbols = {
    'skull': {
        'value': '"skull": what is the number of Monster enemies in play? Press a "num" and "enter" '},
    'cultist': {
        'value': -2,
        'instant effect': 'place 1 doom on the nearest enemy'},
    'tablet': {
        'value': -3,
        'instant effect': 'If there is a Monster enemy at your location, take 1 damage'},
    'Elder Thing': {
        'value': -5,
        'reveal': '"Elder Thing": is there an Ancient One enemy in play? Press "y" or "n" and "enter" '}
}

# The Night of a Zealot standard
The_Night_of_Zealot_standard = {
    'The Gathering': {
        'bag': The_Night_of_Zealot_standard_bag,
        'symbols': The_Gathering_standard_symbols},

    'The Midnight Masks': {
        'bag': The_Night_of_Zealot_standard_bag,
        'symbols': The_Midnight_Masks_standard_symbols},

    'The Devourer Below': {
        'bag': The_Devourer_Below_standard_bag,
        'symbols': The_Devourer_Below_standard_symbols},
}

# ALL CAMPAIGNS DICT

camp_dict = {'The Night of a Zealot standard': The_Night_of_Zealot_standard}


# collect a bag for game like a list with tuples(name, (value, reveal=''))
def chaos_bag_for_pulling(campaign, scenario, player):

    scenario_data = camp_dict[campaign][scenario]
    chaos_bag_keys = scenario_data['bag']
    chaos_bag_symbols = scenario_data['symbols']
    token_like_tuple_list = []
    el = 0

    while el < len(chaos_bag_keys):

        token_name = chaos_bag_keys[el]

        if token_name in chaos_bag_symbols:
            token_value = chaos_bag_symbols[token_name]['value']
            print(chaos_bag_symbols[token_name])

            if type(token_value) == str:
                if 'Press a "num" and "enter"' in token_value:
                    token_value = -int(ICh(N_in_C(token_value), 'num'))

            if 'reveal' in chaos_bag_symbols[token_name]:
                print(token_name)
                if type(chaos_bag_symbols[token_name]['reveal']) == str:
                    reveal_q = chaos_bag_symbols[token_name]['reveal']
                    reveal_flag = True if ICh(N_in_C(reveal_q)) == 'y' else False
                else:
                    reveal_flag = True

                token_value = (token_value, 'reveal') if reveal_flag else token_value

        elif token_name == 'Elder Sign':
            token_value = Elder_Sign(player)

        elif token_name == 'Auto-fail':
            token_value = -99

        else:
            token_value = int(token_name)

        count_of_similar = chaos_bag_keys.count(token_name)
        token_like_tuple_list.extend([(token_name, token_value)]*count_of_similar)

        el += count_of_similar

    return token_like_tuple_list


# find an instant effect of token return str
def instant_effect(campaign, scenario, token_name):
    if 'instant effect' in camp_dict[campaign][scenario]['symbols'][token_name]:
        return camp_dict[campaign][scenario]['symbols'][token_name]['instant effect']


# find a fail effect of token(s) return list
def if_fail(campaign, scenario, reveal_token_list):
    if_fail_list = []
    for token in reveal_token_list:
        if 'fail' in camp_dict[campaign][scenario]['symbols'][token]:
            if_fail_list.append(camp_dict[campaign][scenario]['symbols'][token]['fail'])
    return if_fail_list


def main():
    if __name__ == '__main__':
        # print(chaos_bag_for_pulling('The Night of a Zealot standard', 'The Devourer Below', 'Roland Banks'))
        # print(instant_effect('The Night of a Zealot standard', 'The Devourer Below', 'cultist'))
        print(if_fail('The Night of a Zealot standard', 'The Midnight Masks', ['tablet', 'skull']))


main()
