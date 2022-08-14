from game_data.colored_keywords import text_in_color, names_in_color as N_in_C
from game_data.input_checking import input_checking as ICh
from funcs_for_input import change_a_player, find_a_player, find_a_scenario, input_skill_test, input_skill
from tablica import succeed_or_fail_list, table
from game_data.fast_token_value import chaos_bag_for_pulling, chaos_bag_for_probability, keys_dict
from game_data.prob_funcs import result_cycle
from random import choice
from datetime import datetime


print(text_in_color('\nHi! Welcome to a Probability Utility!\n', 'fat'))

date = datetime.today()
date_normalize = date.strftime('%d.%m.%Y')
time = datetime.now()
time_normalize = time.strftime('%H:%M')

q_start = text_in_color('How many players are? ', 'fat')
count_of_players = int(ICh(q_start, 'num'))

Investigators = find_a_player(count_of_players)
print('')
scenario = find_a_scenario()
print('')

# для записи в логах
if len(Investigators) > 1:
    other_investigators_in_str = ', '.join(Investigators[1:])
    coop_game = f'Other investigator(s) is(are) {other_investigators_in_str}'
else:
    coop_game = 'Solo game'


# запись в логах!
logs = open('logs/logs.txt', 'w')
logs.write(
    f'''{date_normalize}
     
{time_normalize} New game is started 
      Lead investigator is {Investigators[0]}.
      {coop_game}
      Scenario is {scenario}
          
''')
logs.close()


flags = {
    'input player': True, 'input skill': True, 'input skill test': True, 'input chaos bag': True
    }

change_a_flag = {
    'change the investigator': 'input player',
    'change a skill': 'input skill',
    'change a skill test': 'input skill test',
    'change a values of some tokens in the chaos bag': 'input chaos bag',
    'change all': 'all',
    'no changes': 'exit'
    }
if len(Investigators) < 2:
    del change_a_flag['change the investigator']

# блок инпута
game_flag = True

while game_flag:
    while flags['input player']:
        player = change_a_player(Investigators)
        flags['input player'] = False
    while flags['input skill']:
        skill = input_skill(player)
        flags['input skill'] = False
    while flags['input skill test']:
        skill_test = input_skill_test()
        flags['input skill test'] = False
    while flags['input chaos bag']:
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        flags['input chaos bag'] = False


# блок подсчета вероятности
    result = skill - skill_test
    print('')
    print(N_in_C(player))
    print(text_in_color(f'Skill is {skill} points. \nSkill test is {skill_test}. \nResult is {result}'))
    chaos_bag_values = chaos_bag_for_probability(chaos_bag)
    succeed_or_fail_result_percent_tuple_list = [
        result_cycle(chaos_bag_values, i) for i in succeed_or_fail_list if 'succeed' in i[1]
            ]
    fail_result_percent_tuple_list = [
        result_cycle(chaos_bag_values, i, skill_test) for i in succeed_or_fail_list if 'fail' in i[1]
            ]
    succeed_or_fail_result_percent_tuple_list.extend(fail_result_percent_tuple_list)
    table(succeed_or_fail_result_percent_tuple_list, result)
    # print(succeed_or_fail_result_percent_tuple_list[0][0][1])



    # для записи в логах
    time_of_checking = time.now()
    time_of_checking = time_of_checking.strftime('%H:%M')
    succeed_by_0 = [i[1] for i in result_cycle(chaos_bag_values, succeed_or_fail_list[0])[0] if i[0] == str(result)]

    # запись в логах
    logs = open('logs/logs.txt', 'a')
    logs.write(
        f'''{time_of_checking} {player} has a skill test. {skill} vs {skill_test} (skill vs skill test). 
      Result is {result}. Probability of success is {succeed_by_0[0]}%
      
''')
    logs.close()

   
# блок тяни жетончик
    print('')
    q_pull_token = (N_in_C(f'Does {player} is ready to pull a chaos token? press "y" or "n" and "enter" '))
    if ICh(q_pull_token) == 'y': # вход в блок
        bag_for_reveal = []
        bag_for_reveal.extend(chaos_bag)
        reveal_flag = True
        token_value = 0
        tokens = []
        while reveal_flag:
            token = choice(bag_for_reveal)
            token_name = f'"{token[0]}"'
            pull_token_value = token[1] if type(token[1]) == int else token[1][0]
            tokens.append(token_name)
            token_value += pull_token_value
            if type(token[1]) != int:
                bag_for_reveal.remove(token)
                print(N_in_C(f'{token[0]} is pulled. Value is {token[1][0]}. You must reveal another token'))
            else:
                reveal_flag = False
                tokens_in_str = ', '.join(tokens)
                is_plural = 'are' if len(tokens) > 1 else 'is'
                last_result = result + token_value
        
        print(N_in_C(f'{tokens_in_str} {is_plural} pulled. Value is {token_value}. Result is {last_result}'))
        
        if last_result >= 0:
            total = f' succeed the skill test by {last_result}'
            print(N_in_C(player) + text_in_color(total, 'green'))
        else:
            total = f' fail the skill test by {last_result}'
            print(N_in_C(player) + text_in_color(total, 'red'))

        # для записи в логах
        time_of_pulling = time.now()
        time_of_pulling = time_of_pulling.strftime('%H:%M')

        # запись в логах
        logs = open('logs/logs.txt', 'a')
        logs.write(
            f'''{time_of_pulling} {tokens_in_str} {is_plural} pulled. 
      Value is {token_value}. Result is {last_result}
      {player}{total}
      
''')
        logs.close()


# блок возврата к началу
    print('')
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
            elif change_a_flag[changes_dict[answer]] == 'all':
                flags = {key: True for key in flags}
                break
            else:
                flags[change_a_flag[changes_dict[answer]]] = True
            
#        print(flags)

