from game_data.colored_keywords import text_in_color
from game_data.input_checking import input_checking as ICh
from probability import change_a_player, fund_a_player, find_a_scenario, input_skill_test, input_skill


# print(text_in_color('\nHi! Welcome to a Probability Utility!\n', 'fat'))

# q_start = text_in_color('How many players are? ', 'fat')
# count_of_players = int(ICh(q_start, 'num'))

# Investigators = fund_a_player(count_of_players)
# scenario = find_a_scenario()

input_flag = True

Investigators = ['1']
while input_flag == True:
    input_player_flag = True
    while input_player_flag == True:
        player = change_a_player(Investigators)
        skill_test = input_skill_test()
        skill = input_skill(player)
        q_input_flag = 'Do you want to change some values? '
        input_flag = True if ICh(q_input_flag) == 'y' else False

print('no input')
