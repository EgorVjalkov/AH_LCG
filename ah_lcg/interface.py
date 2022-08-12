from game_data.colored_keywords import text_in_color, names_in_color as N_in_C
from game_data.input_checking import input_checking as ICh
from probability import change_a_player, find_a_player, find_a_scenario, input_skill_test, input_skill
from tablica import succeed_or_fail_list, table
from game_data.fast_token_value import chaos_bag_for_pulling, chaos_bag_for_probability, keys_dict
from game_data.prob_funcs import result_cycle


print(text_in_color('\nHi! Welcome to a Probability Utility!\n', 'fat'))

q_start = text_in_color('How many players are? ', 'fat')
count_of_players = int(ICh(q_start, 'num'))

Investigators = find_a_player(count_of_players)
scenario = find_a_scenario()


flags = {
    'input player': True, 'input skill': True, 'input skill test': True, 'input chaos bag': True
    }

change_a_flag = {
    'change the investigator': 'input player', 
    'change a skill': 'input skill',
    'change a skill test': 'input skill test', 
    'change a values of some tokens in the chaos bag': 'input chaos bag',
    'don`t want to change': 'exit'
    }

# блок инпута
game_flag = True
while game_flag == True:
    while flags['input player'] == True:
        player = change_a_player(Investigators)
        flags['input player'] = False
    while flags['input skill'] == True:
        skill = input_skill(player)
        flags['input skill'] = False
    while flags['input skill test'] == True:
        skill_test = input_skill_test()
        flags['input skill test'] = False
    while flags['input chaos bag'] == True:
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        flags['input chaos bag'] = False

# блок подсчета вероятности        
    result = skill - skill_test
    print('')
    print(N_in_C(player))
    print(text_in_color(f'Skill is {skill} points. \nSkill test is {skill_test}. \nResult is {result}'))
    chaos_bag_values = chaos_bag_for_probability(chaos_bag)
    print(chaos_bag_values)
    succeed_or_fail_result_percent_tuple_list = [
        result_cycle(chaos_bag_values, i) for i in succeed_or_fail_list if 'succeed' in i[1]
            ]
    fail_result_percent_tuple_list = [
        result_cycle(chaos_bag_values, i, skill_test) for i in succeed_or_fail_list if 'fail' in i[1]
            ]
    succeed_or_fail_result_percent_tuple_list.extend(fail_result_percent_tuple_list)
    table(succeed_or_fail_result_percent_tuple_list, result)


# блок выбора инпута
    q_input_flag = text_in_color('Do you want to change some values? ', 'fat')
    if ICh(q_input_flag) == 'y':
        changes_dict = dict(enumerate(change_a_flag, 1))
        limit_of_answer = tuple(str(i) for i in range(1, len(changes_dict) + 1))
        while True:
            for key in changes_dict:
                print(f'press "{key}" and "enter" - {changes_dict[key]}')
            q_change_player = text_in_color('What do you change? ', 'fat')
            answer = int(ICh(q_change_player, limit_of_answer))
            if change_a_flag[changes_dict[answer]] == 'exit':
                break
            else:
                flags[change_a_flag[changes_dict[answer]]] = True
            
#    print(flags)

