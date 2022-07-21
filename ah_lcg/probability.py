from game_data.fast_token_value import chaos_bag_values_dict, keys, players
from game_data.input_checking import input_checking as ICh
from game_data.colored_keywords import names_in_color as N_in_C, colored_scenario, colored_points

def short_probability(scenario, player):
    investigators_in_str = ', '.join(players)
    colored_scenario_list = [colored_scenario(i)for i in chaos_bag_values_dict.keys()]
    scenarios_in_str = ', '.join(colored_scenario_list)
    while True: # input check
        if player in players:
            break 
        else: player = input(N_in_C(f'Incorrect investigator. Investigators are {investigators_in_str}\n:'))
    while True: # input check
        if scenario in chaos_bag_values_dict:
            break
        else: scenario = input(f'Incorrect scenario. Scenarios are {scenarios_in_str}\n:')
    q = N_in_C('What`s the difficulty of a skill test? Press "num" and "enter" ')
    skill_test = -ICh(q, 'num') # with check
    q1 = N_in_C(f'What points of the skill does {player} have? Press "num" and "enter" ')
    skill = ICh(q1, 'num') # with check
    result = skill + skill_test
    chaos_bag_values = chaos_bag_values_dict[scenario](player)
    count_of_tokens  = len(chaos_bag_values)
    done = [i+result for i in chaos_bag_values if i+result >= 0]
    success = len(done)
    done_procent = round((success/count_of_tokens) * 100)
    result_in_color = colored_points(result, done_procent) 
    print(f'result is {result_in_color[0]} done_procent is {result_in_color[1]}')
#adding points!!!!!!!!! необходимо сделать диалоговфый  интерфейс 
#    while True: # dialog interface
        print(N_in_C(f'Does {player} need to\n'))
        q2 = 'Press \'y\' or "n" and \'enter\' '
        if input() == 'y':
            for add in range (1, 20):
                new_result = result + add
                new_done = [i+new_result for i in tokens_value if i+new_result >= 0]
                new_success = len(new_done)
                new_done_percent = round((new_success/count_of_tokens) * 100)
                if new_done_percent > 0:
                    print(f'If you add {add} point(s), done_procent is {new_done_percent}%')
                if new_done_percent >= round((count_of_tokens-1) / count_of_tokens * 100):
                    break

scenario = 'The Gathering standard'
player = 'Roland Banks'

short_probability(scenario, player)










# # Outdo 2 points percent
#     if input('Press \'y\' and \'enter\' if you want to count 2 points passed percent. ') == 'y':
#         increase_2 = [i for i in tokens_value if i+result >= 2]
#         success2 = len(increase_2)
#         increase_2_percent = round(success2/count_of_tokens * 100)
#         print(f'2 points passed percent is {increase_2_percent}%')
#     # adding point(s)        
#         if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
#             for add in range (1, 20):
#                 new_result = result + add
#                 new_done = [i+new_result for i in tokens_value if i+new_result >= 2]
#                 new_success = len(new_done)
#                 new_done_percent = round((new_success/count_of_tokens) * 100)
#                 if new_done_percent > 0:
#                     print(f'if you add {add} point(s), 2 points passed percent is {new_done_percent}%')
#                 if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
#                     break
# # Outdo 4 points percent
#     if input('Press \'y\' and \'enter\' if you want to count 4 points passed percent. ') == 'y':
#         increase_4 = [i for i in tokens_value if i+result >= 4]
#         success4 = len(increase_4)
#         increase_4_percent = round(success4/count_of_tokens * 100)
#         print(f'4 points passed percent is {increase_4_percent}%')
#     # adding point(s)        
#         if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
#             for add in range (1, 20):
#                 new_result = result + add
#                 new_done = [i+new_result for i in tokens_value if i+new_result >= 4]
#                 new_success = len(new_done)
#                 new_done_percent = round((new_success/count_of_tokens) * 100)
#                 if new_done_percent > 0:
#                     print(f'if you add {add} point(s), 4 points passed percent is {new_done_percent}%')
#                 if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
#                     break                
# # for crystal_pendulum
#     if input('Press \'y\' and \'enter\' if you try to use the crystal pendulum. ') == 'y':
#         add_point = input('Add any point(s) if you want to correct your skill ' )
#         if not add_point.isdigit(): add_point = 0
#         correction = int(add_point) + result
#         abs_chaos_bag = [abs(i+correction) for i in tokens_value]
#     #auto-fail correction
#         abs_chaos_bag.remove(99-correction)
#         abs_chaos_bag.append(check)
#         print(abs_chaos_bag)
#         for_crystal_pendulum = {}
#         for i in abs_chaos_bag:
#             for_crystal_pendulum[i] = abs_chaos_bag.count(i)
#         max = 1
#         for i in for_crystal_pendulum.items():
#             if max < i[1]:
#                 max = i[1]
#                 num = i[0]
#         probe = round(max/len(chaos_bag), 2) * 100
#         print(f'number for crystal pendulum = {num}, probability is {probe}%')