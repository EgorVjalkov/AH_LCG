from random import choice
from ah_lcg.funcs.colored_keywords import text_in_color, names_in_color as N_in_C
from ah_lcg.funcs.input_checking import input_checking as ICh
from ah_lcg.funcs.tablica import succeed_or_fail_list, table
from ah_lcg.game_data.fast_token_value import chaos_bag_for_pulling, chaos_bag_for_probability, keys_dict
from ah_lcg.funcs.prob_funcs import result_cycle
from ah_lcg.funcs.funcs_for_input import (change_a_player,
                                          find_a_player,
                                          find_a_scenario,
                                          input_skill_test,
                                          input_skill,
                                          add_points,
                                          dialog_interface)
from ah_lcg.logs.func_for_writing_logs import write_a_log


# ПРОТЕСТРУЙ С СУМКОЙ ПОЛНОЙ ФАЙЛОВ ИЛИ УСПЕХОВ
# ЧТЕНИЕ ЛОГОВ ИЗ csv
# ЗАМУТ С ФЛАГАМИ В ПОБОЧНОМ МЕНЮ

# приветствие
print(text_in_color('\nHi! Welcome to Probability Utility for Arkham Horror LCG!\n', 'fat'))


# новая игра: ввод сыщиклв и сценария
q_start = text_in_color('How many players are? ', 'fat')
count_of_players = int(ICh(q_start, 'num'))

Investigators = find_a_player(count_of_players)
print('')
scenario = find_a_scenario()
print('')


# запись в логах
write_a_log['start game'](scenario, Investigators)


# переключатели на введение данных
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


# блок первичного инпута
game_flag = True

while game_flag:
    while flags['input player']:
        player = change_a_player(Investigators)
        flags['input player'] = False
        print('')
    while flags['input skill']:
        skill = input_skill(player)
        flags['input skill'] = False
    while flags['input skill test']:
        skill_test = input_skill_test()
        flags['input skill test'] = False
    while flags['input chaos bag']:
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        flags['input chaos bag'] = False


# переключатели

    recalculate_flags = {'result': True, 'bag': True}

    pull_token_flag = True
    re_input_flag = True


# блок подсчета вероятности
    while recalculate_flags['result']:
        result = skill - skill_test

    while recalculate_flags['bag']:
        chaos_bag_values = chaos_bag_for_probability(chaos_bag)

        f_succeed = lambda i: result_cycle(result, chaos_bag_values, i)
        list_for_table = [f_succeed(i) for i in succeed_or_fail_list if 'succeed' in i[1]]

        f_fail = lambda i: result_cycle(result, chaos_bag_values, i, skill_test)
        fail_list = [f_fail(i) for i in succeed_or_fail_list if 'fail' in i[1]]

        list_for_table.extend(fail_list)

    # вывод результатов на экран
        print('')
        print(N_in_C(player))
        print(text_in_color(f'Skill is {skill} points. \nSkill test is {skill_test}. \nResult is {result}'))
        table(list_for_table, result)


    # запись в логах
        list_by_0 = result_cycle(result, chaos_bag_values, (0, 'succeed by 0'))[0]
        succeed_by_0 = [i[1] for i in list_by_0 if i[0] == str(result)]
        write_a_log['checking'](player, skill, skill_test, succeed_by_0)

    # вход в побочное меню
        print(N_in_C(f'What does {player} try to do now?'))


    # переключатели в меню
        flags_before_token = {'add points': False}
        questions_before_token = {
            'add some skill points': 'add points',
            'pull a token': 'exit',
        }

    # диалоговый интерфэйс
        flags_before_token = dialog_interface(flags_before_token, questions_before_token)


        # добавь очков
        if flags_before_token['add points']:
            add = add_points(player)

        # запись в логах
            write_a_log['adding'](player, add)

            skill += add
            flags_before_token['add points'] = False
            pull_token_flag = False
            re_input_flag = False

    print('')

    # блок тяни жетончик
    if pull_token_flag:
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
                print(N_in_C(f'{token_name} is pulled. Value is {token[1][0]}. You must reveal another token'))
            else:
                reveal_flag = False
                tokens_in_str = '=>'.join(tokens)
                is_plural = 'are' if len(tokens) > 1 else 'is'
                last_result = result + token_value

        # по отдельным жетонам
        if "Auto-fail" in tokens_in_str:
            last_result = -skill_test
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. {player}`s skill is 0. Result is {last_result}'))
        elif "Elder Sign" in tokens_in_str and token_value > 50:
            last_result = skill
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. skill test is 0. Result is {last_result}'))
        else:
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. Value is {token_value}. Result is {last_result}'))

        # интерпретация результата
        if last_result >= 0:
            total = f' succeed the skill test by {last_result}'
            print(N_in_C(player) + text_in_color(total, 'green'))
        else:
            total = f' fail the skill test by {abs(last_result)}'
            print(N_in_C(player) + text_in_color(total, 'red'))


        # запись в логах
        write_a_log['revealing'](player, tokens_in_str, token_value, last_result, total)


    # блок возврата к вводу параметров
    print('')
    if re_input_flag:
        q_re_input_flag = text_in_color('Do you want to change some values? ', 'fat')
        if ICh(q_re_input_flag) == 'y':
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
