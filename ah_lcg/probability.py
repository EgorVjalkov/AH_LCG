from game_data.fast_token_value import chaos_bag_values_dict, keys, players
from game_data.input_checking import input_checking as ICh
from game_data.colored_keywords import names_in_color as N_in_C, colored_scenario, colored_points
from game_data.dialog_interface import side_menu, general_menu
from game_data.prob_funcs import done_percent as dp, success_counting_points_cycle as S_CP_cy

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


#первичный результат
result_in_color = colored_points(result, dp(result, chaos_bag_values))
print(f'\nresult is {result_in_color[0]} success percent is {result_in_color[1]}\n')

#первичный "если ты добавишь столько - процент будет столько" 
points_to_percent_list = S_CP_cy(result, chaos_bag_values)
for tup in points_to_percent_list:
    colored_tup = colored_points(tup[0], tup[1])
    print(f'If you add {colored_tup[0]} point(s), success percent is {colored_tup[1]}')
    

#диалоговый интерфейс
GENERAL_MENU_FLAG = True

if GENERAL_MENU_FLAG == True:
#основное меню    
    print(N_in_C(f'\nWhat does {player} need to do?'))
    for key in general_menu:
        print(N_in_C(f'press "{key}" and "enter" - {general_menu[key]}'))
    q_GM = ': ' # input check
    answer = ICh(q_GM, ('1','2','3')) # input check
#выбор варианта ответа
    if answer == '2':
        GENERAL_MENU_FLAG = False # переход к жетонам
    if answer == '1': 
        q_adding = N_in_C(f'How many points does {player} add? ')
        result += ICh(q_adding, 'num')
        result_in_color = colored_points(result, dp(result, chaos_bag_values))
        print(f'result is {result_in_color[0]} success percent is {result_in_color[1]}\n')
        GENERAL_MENU_FLAG = False # переход к жетонам
    if answer == '3':
        SIDE_MENU_FLAG = True # переход в побочное меню
        while SIDE_MENU_FLAG == True:
            num_of_suc_or_fail = side_menu() # вернет int или tup
            if num_of_suc_or_fail == 'exit':
                SIDE_MENU_FLAG = False
            else:
                if type(num_of_suc_or_fail) == int:
                    points_to_percent_list = S_CP_cy(result, chaos_bag_values, num_of_suc_or_fail)
                    for tup in points_to_percent_list:
                        colored_tup = colored_points(tup[0], tup[1])
                        print(f'If you add {colored_tup[0]} point(s), success percent is {colored_tup[1]}')
                else: 


print(result,)
# #adding points!!!!!!!!! необходимо сделать диалоговфый  интерфейс для 3 ог этапа
# #    while True: # dialog interface
#         print(N_in_C(f'Does {player} need to\n'))
#         q2 = 'Press \'y\' or "n" and \'enter\' '
#         if input() == 'y':










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