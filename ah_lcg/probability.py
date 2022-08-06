from game_data.fast_token_value import  keys_dict, players, chaos_bag_for_probability, chaos_bag_for_pulling
from game_data.input_checking import input_checking as ICh
from game_data.colored_keywords import names_in_color as N_in_C, colored_scenario, colored_points, text_in_color
from game_data.dialog_interface import menu, general_menu, card_using_menu_dict
from game_data.prob_funcs import counting_points_cycle as CP_Cy
from random import choice
#НЕОБХОДИМО!!!!! ПРИ ПЕЧАТИ РЕЗУЛЬТАТА УКАЗЫВАТЬ КАКОЙ ЭТО РЕЗУЛЬТАТ. дОБАВИТЬ СРАВНЕНИЕ, ЧТОБ ЗНАТЬ ФАЙЛ ИЛЬ СУКЦЕСС
# сценарий
scenario = 'The Gathering standard'
players_list = ('Winifred Habbamock', 'Stella Clark')

# приветствие
print(text_in_color('\nHi! Welcome to a Probability Utility!\n', 'fat'))

# # поиск игрока по первым буквам
# while True ###########
#     start_of_name = input('Input a few first letters of investigator`s name and press "enter" ')
#     filtred_players = [i for i in players if start_of_name in i[:len(start_of_name)]]
#     if len(filtred_players) > 1:
#         q_name = N_in_C(f'Who you mean? Press "num" and "enter" ')
#         player = ICh(q_name, 'num')
#         print(player)
#     filtred_players_in_str = N_in_C(' or '.join(filtred_players))

# Выбор игрока из кортежа играющих
if len(players_list) > 1:
    players_dict = dict(enumerate(players_list, 1))
    for key in players_dict:
        print(N_in_C(f'press "{key}" and "enter" - {players_dict[key]}'))
    limit_of_answer = tuple(str(i) for i in range(1, len(players_list)+1))
    q_change_player = text_in_color(f'Who passes a skill test? ', 'fat')
    answer = int(ICh(q_change_player, limit_of_answer))
    player = players_dict[answer]
else: player = players_list[0]
print(N_in_C(f'\n{player} passes a skill test\n'))


# # проверка исходных данных
# investigators_in_str = '\n'.join(players)
# colored_scenario_list = [colored_scenario(i)for i in chaos_bag_values_dict.keys()]
# scenarios_in_str = ', '.join(colored_scenario_list)
# while True: 
#     if player in players:
#         break 
#     else: player = input(N_in_C(f'Incorrect investigator. Investigators are {investigators_in_str}\n:'))
# while True:
#     if scenario in chaos_bag_values_dict:
#         break
#     else: scenario = input(f'Incorrect scenario. Scenarios are {scenarios_in_str}\n:')
    

#ввод данных проверки и уровня навыка    
q = N_in_C('What`s the difficulty of a skill test? Press "num" and "enter" ')
skill_test = int(ICh(q, 'num')) # with check

q1 = N_in_C(f'What points of the skill does {player} have? Press "num" and "enter" ')
skill = int(ICh(q1, 'num')) # with check
print('')


#расчет результата и коррекция значения жетонов(от сценария и сыщика)
result = skill - skill_test
chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
chaos_bag_values = chaos_bag_for_probability(chaos_bag)


#первичный результат
result_in_color = colored_points(result, CP_Cy(result, chaos_bag_values)[0][1])
print(f'\nresult is {result_in_color[0]} success percent is {result_in_color[1]}\n')


#блок переменных для нулевой проверки
num = (0, 'succeed')
q_how_many = N_in_C(f'How many points can {player} add? ')
add_points = int(ICh(q_how_many, 'num'))


#диалоговый интерфейс
GENERAL_MENU_FLAG = True
while GENERAL_MENU_FLAG == True: #основное меню
    
    #подстчет вероятностей при добавлении всех возможных очков
    if num != 'exit':
        points_to_percent_list = CP_Cy(result, chaos_bag_values, num, add_points, skill_test)
        for tup in points_to_percent_list:
            noncolor_points = tup[0]
            colored_tup = colored_points(tup[0], tup[1])
            print(f'If you add {colored_tup[0]} point(s), success percent is {colored_tup[1]}')
        if noncolor_points < add_points:
            print(N_in_C(player) + text_in_color(' needn`t add more points!', 'green'))
        print('')

    # первичный результат получен, далее ответ от игрока
    answer = menu(general_menu, player)
    if answer == 'exit': 
        break #все устроило, переход к жетонам
    result_of_menu = answer(player)
    if type(result_of_menu) == int:
        result += result_of_menu
        result_in_color = colored_points(result, CP_Cy(result, chaos_bag_values)[0][1])
        print(f'\nresult is {result_in_color[0]} success percent is {result_in_color[1]}\n')
        GENERAL_MENU_FLAG = False # добавлены очки навыка, переход к жетонам
    else:
        num = result_of_menu # побочное меню

 
#тянем жетоны
print('') 
token = choice(chaos_bag)
if type(token[1]) == list:
    print(N_in_C(f'{token[0]} is pulled. Value is. You need to pull another token')) #ты остановился на переменной жетона!
    chaos_bag_keys_with_tokens.remove(token)
    another_token = choice(chaos_bag_keys_with_tokens)
    print(N_in_C(f'{another_token[0]} is pulled'))
print(N_in_C(f'{token[0]} is pulled. Value is {token[1]}. Result is {result+token[1]}'))
if (result+token[1]) >= 0:
    print(N_in_C(player) + text_in_color(f' succeed the skill test by {result+token[1]}', 'green'))
else: print(N_in_C(player) + text_in_color(f' failed the skill test by {result+token[1]}', 'red'))


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