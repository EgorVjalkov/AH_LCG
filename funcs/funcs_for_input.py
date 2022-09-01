from game_data.fast_token_value import keys_dict, players
from funcs.input_checking import input_checking as ICh
from funcs.colored_keywords import names_in_color as N_in_C, colored_scenario, text_in_color


# поиск игроков по имени
def find_a_player(count_of_players):

    Investigators = []
    players_copy = list(players)

    while len(Investigators) < count_of_players:

        while True:

            # поиск по буквам
            if len(Investigators) == 0:
                q = text_in_color(
                    'Input a few first letters of a lead investigator`s name and press "enter" or write "all" ', 'fat'
                )
                start_of_name = ICh(q, 'l')
            else:
                q = text_in_color('Input a few first letters of investigator`s name and press "enter" or write "all" ',
                                  'fat')
                start_of_name = ICh(q, 'l')

            # поиск для всех
            if start_of_name == 'all':
                filtred_players = [i for i in players_copy]
            # фильтрация
            else:
                filtred_players = [i for i in players_copy if start_of_name.lower() in i[:len(start_of_name)].lower()]

            if not filtred_players:
                filtred_players = [i for i in players_copy if start_of_name.lower() in i.lower()]

            # подтверждение для одного
            if len(filtred_players) == 1:
                q = N_in_C(f'Do you mean {filtred_players[0]}? ')
                start_of_name = ICh(q)

                if start_of_name == 'y':
                    player = filtred_players[0]
                    del players_copy[players_copy.index(player)]
                    break

            # выбор из нескольких
            elif len(filtred_players) > 1:

                if start_of_name != 'all':
                    filtred_players.append('none of them')

                menu_dict = dict(enumerate(filtred_players, 1))
                limit_of_answer = tuple(str(i) for i in range(1, len(filtred_players) + 1))

                for key in menu_dict:
                    print(N_in_C(f'press "{key}" and "enter" - {menu_dict[key]}'))

                q_change_player = text_in_color(f'Who you mean? ', 'fat')
                answer = int(ICh(q_change_player, limit_of_answer))
                player = menu_dict[answer]
                del players_copy[players_copy.index(player)]
                break

        Investigators.append(player)

        if len(Investigators) == 1:
            print(N_in_C(f'You changed {player} as the lead investigator\n'))
        else:
            print(N_in_C(f'You changed {player}\n'))

    return Investigators


# поиск сценария по имени
def find_a_scenario():

    while True:
        q_start_of_name = text_in_color(
            'Input a few first letters of a name of scenario !without article! and press "enter" or write "all" ',
            'fat')
        start_of_name_scenario = ICh(q_start_of_name, 'l')
        # поиск для всех
        if start_of_name_scenario == 'all':
            scenario_list = list(keys_dict.keys())
            # фильтрация
        else:
            scenario_list = [i for i in list(keys_dict.keys()) if
                             start_of_name_scenario.lower() in i[4:4 + len(start_of_name_scenario)].lower()]
        if not scenario_list:
            scenario_list = [i for i in list(keys_dict.keys()) if start_of_name_scenario.lower() in i.lower()]

            # подтверждение для одного
        if len(scenario_list) == 1:
            q = f'Do you mean {colored_scenario(scenario_list[0])}? '
            start_of_name_scenario = ICh(q)

            if start_of_name_scenario == 'y':
                scenario = scenario_list[0]
                break

                # выбор из нескольких
        elif len(scenario_list) > 1:

            if start_of_name_scenario != 'all':
                scenario_list.append('none of that')

            menu_dict = dict(enumerate(scenario_list, 1))
            for key in menu_dict:
                print(f'press "{key}" and "enter" - {colored_scenario(menu_dict[key])}')

            limit_of_answer = tuple(str(i) for i in range(1, len(scenario_list) + 1))
            q_change_scenario = text_in_color(f'What do you mean? ', 'fat')
            answer = int(ICh(q_change_scenario, limit_of_answer))

            scenario = menu_dict[answer]
            break

    print(f'Scenario is {colored_scenario(scenario)}\n')

    return scenario


# выбор сыщика
def change_a_player(players_list):
    if len(players_list) > 1:
        players_dict = dict(enumerate(players_list, 1))
        print(text_in_color(f'Who passes a skill test? ', 'fat'))
        for key in players_dict:
            print(N_in_C(f'press "{key}" and "enter" - {players_dict[key]}'))
        limit_of_answer = tuple(str(i) for i in range(1, len(players_list) + 1))
        q_change_player = text_in_color(f'Who you change? ', 'fat')
        answer = int(ICh(q_change_player, limit_of_answer))
        player = players_dict[answer]
    else:
        player = players_list[0]
    print(N_in_C(f'{player} passes a skill test\n'))
    return player


# ввод данных проверки и уровня навыка
def input_skill_test():
    q = N_in_C('What`s the difficulty of a skill test? Press "num" and "enter" ')
    skill_test = int(ICh(q, 'num'))  # with check
    return skill_test


def input_skill(player):
    q1 = N_in_C(f'How many points of the skill does {player} have? Press "num" and "enter" ')
    skill = int(ICh(q1, 'num'))  # with check
    return skill


def add_points(player):
    q_add = N_in_C(f'How many skill points {player} try to add? Press "num" and "enter" ')
    add = int(ICh(q_add, 'num'))
    return add


def use_cards(player):
    return 'there are not any cards now'


def dialog_interface(flag_dict, questions_dict, type_of_dialog='complex', player='', func_dict={}):
    while True:
        questions_dict_copy = questions_dict.copy()
        flag_dict_copy = flag_dict.copy()
        what_done = ''
        result_of_func = {}
        while True:
            questions_dict_enumerate = dict(enumerate(questions_dict_copy, 1))
            limit_of_answer = tuple(str(i) for i in range(1, len(questions_dict_enumerate) + 1))
            for key in questions_dict_enumerate:
                print(f'press "{key}" and "enter" - {questions_dict_enumerate[key]}')

            if not player:
                if what_done:
                    q_change_answer = text_in_color(f'You try to {what_done}. Anything else? ', 'fat')
                else:
                    q_change_answer = text_in_color(f'What do you change? ', 'fat')
            else:
                if what_done:
                    q_change_answer = N_in_C(f'{player} tries to {what_done}. Anything else? ')
                else:
                    q_change_answer = N_in_C(f'What does {player} change? ')

            answer = int(ICh(q_change_answer, limit_of_answer))
            questions_dict_key = questions_dict_enumerate[answer]
            questions_dict_value = questions_dict_copy[questions_dict_key]

            if type_of_dialog == 'simple':
                flag_dict[questions_dict_value] = not flag_dict[questions_dict_value]
                if not player:
                    print(text_in_color(f'You change {questions_dict_key}\n', 'fat'))
                else:
                    print(N_in_C(f'{player} changes {questions_dict_key}\n'))
                return flag_dict

            if questions_dict_value == 'exit':
                result_of_func['flags'] = flag_dict
                return result_of_func

            elif questions_dict_value == 'all':
                flag_dict = {key: not flag_dict_copy[key] for key in flag_dict_copy}
                result_of_func['flags'] = flag_dict
                return result_of_func

            elif questions_dict_value == 'reset':
                if flag_dict != flag_dict_copy:
                    flag_dict = flag_dict_copy
                    break

            else:
                flag_dict[questions_dict_value] = not flag_dict[questions_dict_value]
                comma = ', ' if what_done else ''
                if func_dict:
                    result_of_func[questions_dict_value] = func_dict[questions_dict_value](player)
                    what_done += f'{comma}{questions_dict_key}: {result_of_func[questions_dict_value]}'
                else:
                    what_done += f'{comma}{questions_dict_key}'
                del questions_dict_copy[questions_dict_key]


def func_from_key_and_switch_flag(flag_dict, func_dict, args):
    results_dict = {}
    for key in flag_dict:
        if flag_dict[key]:
            results_dict[key] = func_dict[key](*args)
            flag_dict[key] = not flag_dict[key]
    return results_dict


def main():
    if __name__ == '__main__':
        # CALCULATE = {'result': False, 'bag': False}
        # questions = {
        #     'add some skill points': 'result',
        #     'use cards': 'bag',
        #     'all': 'all',
        #     'reset all changes': 'reset',
        #     'recalculate a probability': 'exit'
        # }
        # funcs = {'result': add_points, 'bag': use_cards}


        # flags = {
        #     'input player': False, 'input skill': False, 'input skill test': False, 'input chaos bag': False
        # }
        #
        # change_a_flag = {
        #     'change the investigator': 'input player',
        #     'change a skill': 'input skill',
        #     'change a skill test': 'input skill test',
        #     'change a value of tokens in the chaos bag': 'input chaos bag',
        #     'change all': 'all',
        #     'reset all changes': 'reset',
        #     'proceed to a new skill test': 'exit'
        # }
        #
        flags_2 = {'pull token': False, 'recalculate': False}
        quest_2 = {'pull a token': 'pull token', 'add points or use cards': 'recalculate'}

        result_of_dialog = dialog_interface(flags_2, quest_2, 'simple')
        print(result_of_dialog)
        print(flags_2)


main()
