from game_data.fast_token_value import chaos_bag_values_dict, keys, players
from game_data.input_checking import input_checking as ICh
from game_data.colored_keywords import names_in_color as N_in_C, colored_scenario, colored_points, text_in_color
from game_data.dialog_interface import menu, general_menu, card_using_menu_dict
from game_data.prob_funcs import counting_points_cycle as CP_Cy
from random import choice

#исходные данные
scenario = 'The Gathering standard'
player = 'Roland Banks'


#проверка исходных данных
investigators_in_str = ', '.join(players)
colored_scenario_list = [colored_scenario(i)for i in chaos_bag_values_dict.keys()]
scenarios_in_str = ', '.join(colored_scenario_list)
while True: 
    if player in players:
        break 
    else: player = input(N_in_C(f'Incorrect investigator. Investigators are {investigators_in_str}\n:'))
while True:
    if scenario in chaos_bag_values_dict:
        break
    else: scenario = input(f'Incorrect scenario. Scenarios are {scenarios_in_str}\n:')
    

#ввод данных проверки и уровня навыка    
q = N_in_C('What`s the difficulty of a skill test? Press "num" and "enter" ')
skill_test = -ICh(q, 'num') # with check

q1 = N_in_C(f'What points of the skill does {player} have? Press "num" and "enter" ')
skill = ICh(q1, 'num') # with check
print('')


#расчет результата и коррекция значения жетонов(от сценария и сыщика)
result = skill + skill_test
chaos_bag_values = chaos_bag_values_dict[scenario](player)
chaos_bag_keys_with_tokens = zip(keys[scenario],chaos_bag_values)


#первичный результат
result_in_color = colored_points(result, CP_Cy(result, chaos_bag_values)[0][1])
print(f'\nresult is {result_in_color[0]} success percent is {result_in_color[1]}\n')

#подстчет вероятностей по имеющимся нвыкам 
q_how_many = N_in_C(f'How many points can {player} add? ')
add_points = ICh(q_how_many, 'num')
points_to_percent_list = CP_Cy(result, chaos_bag_values, (0, 'succeed'), add_points)
for tup in points_to_percent_list:
    noncolor_points = tup[0]
    colored_tup = colored_points(tup[0], tup[1])
    print(f'If you add {colored_tup[0]} point(s), success percent is {colored_tup[1]}')
if noncolor_points < add_points:
    print(N_in_C(player) + text_in_color(' needn`t add more points!', 'green'))
    

#диалоговый интерфейс
# GENERAL_MENU_FLAG = True

# if GENERAL_MENU_FLAG == True:
# #основное меню    
#     print(N_in_C(f'\nWhat does {player} need to do?'))
#     for key in general_menu:
#         print(N_in_C(f'press "{key}" and "enter" - {general_menu[key]}'))
#     q_GM = ': ' # input check
#     answer = ICh(q_GM, ('1', '2' , '3', '4')) # input check
# #выбор варианта ответа
#     if answer == '2':
#         GENERAL_MENU_FLAG = False # переход к жетонам
#     if answer == '1': 
#         q_adding = N_in_C(f'How many points does {player} add? ')
#         result += ICh(q_adding, 'num')
#         result_in_color = colored_points(result, dp(result, chaos_bag_values))
#         print(f'result is {result_in_color[0]} success percent is {result_in_color[1]}\n')
#         GENERAL_MENU_FLAG = False # переход к жетонам
#     if answer == '3':
#         SIDE_MENU_FLAG = True # переход в побочное меню
#         while SIDE_MENU_FLAG == True:
#             num_of_suc_or_fail = side_menu() # вернет int или tup
#             if num_of_suc_or_fail == 'exit':
#                 SIDE_MENU_FLAG = False
#             else:
#                 if type(num_of_suc_or_fail) == int:
#                     points_to_percent_list = S_CP_cy(result, chaos_bag_values, num_of_suc_or_fail)
#                     for tup in points_to_percent_list:
#                         colored_tup = colored_points(tup[0], tup[1])
#                         print(f'if you add {colored_tup[0]} point(s), success percent is {colored_tup[1]}')
#                 else: pass

#тянем жетоны
chaos_bag_keys_with_tokens = list(chaos_bag_keys_with_tokens)
token = choice(chaos_bag_keys_with_tokens)
if type(token[1]) == list:
    print(N_in_C(f'{token[0]} is pulled. Value is. You need to pull another token')) #ты остановился на переменной жетона!
    chaos_bag_keys_with_tokens.remove(token)
    another_token = choice(chaos_bag_keys_with_tokens)
    print(N_in_C(f'{another_token[0]} is pulled'))
print(N_in_C(f'{token[0]} is pulled. Value is {token[1]}'))




 
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