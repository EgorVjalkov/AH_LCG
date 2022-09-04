from random import choice
from funcs.colored_keywords import text_in_color, names_in_color as N_in_C
from funcs.input_checking import input_checking as ICh
from funcs.tablica import succeed_or_fail_list, table
from game_data.fast_token_value import chaos_bag_for_pulling, chaos_bag_for_probability, keys_dict
from funcs.prob_funcs import result_cycle
from funcs.funcs_for_input import (change_a_player,
                                   find_a_player,
                                   find_a_scenario,
                                   input_skill_test,
                                   input_skill,
                                   add_points,
                                   use_cards,
                                   dialog_interface)
#from ah_lcg.logs.func_for_writing_logs import write_a_log

# НУЖНО СДЕЛАТЬ, ЧТОБ СУМАКА БЕЗ ПЕРЕМЕННЫХ НЕ РАСЧИТЫВАЛАСЬ ЗАНОВО, ТИПА УДАЛИТЬ ЛИШКУ ИЗ ДИАЛОГА

# greetings!
print(text_in_color('\nHi! Welcome to Probability Utility for Arkham Horror LCG!\n', 'fat'))


# new game. Input a count of investigators
q_start = text_in_color('How many players are? Press "num" and "enter" (limit is 4 players) ', 'fat')
player_limit = tuple(str(i) for i in range(1, 5))
count_of_players = int(ICh(q_start, player_limit))
print('')

# finding a investigator
Investigators = find_a_player(count_of_players)

# finding a scenario
scenario = find_a_scenario()

# запись в логах
# write_a_log['start game'](scenario, Investigators)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!MAIN FLAGS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# SKILL_TEST_FLAG
SKILL_TEST = True

# INPUT_FLAGS block
INPUT_FLAGS = {
    'input player': True, 'input skill': True, 'input skill test': True, 'input chaos bag': True
    }

question_INPUT_FLAGS = {
        'change the investigator': 'input player',
        'change a skill': 'input skill',
        'change a skill test': 'input skill test',
        'change a value of tokens in the chaos bag': 'input chaos bag',
        'change all': 'all',
        'reset all changes': 'reset',
        'proceed to a new skill test': 'exit'
    }

if len(Investigators) < 2:
    del question_INPUT_FLAGS['change the investigator']

# CALCULATE FLAGS block
CALCULATE = {'result': True, 'bag': True}

recalculate_questions = {
            'add some skill points': 'result',
            # 'use cards': 'bag',
            'reset all changes': 'reset',
            'recalculate a probability': 'exit'
        }

# value is points of skill
ADD = 0

recalculate_funcs = {'result': add_points, 'bag': use_cards}


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!START A PROGRAM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while SKILL_TEST:

    if True in INPUT_FLAGS.values():

        if INPUT_FLAGS['input player']:
            player = change_a_player(Investigators)
            INPUT_FLAGS['input player'] = False

        print(N_in_C(f'{player} passes a skill test\n'))

        if INPUT_FLAGS['input skill']:
            skill = input_skill(player)
            INPUT_FLAGS['input skill'] = False

        if INPUT_FLAGS['input skill test']:
            skill_test = input_skill_test()
            INPUT_FLAGS['input skill test'] = False

        if INPUT_FLAGS['input chaos bag']:
            chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
            INPUT_FLAGS['input chaos bag'] = False

        print('')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!CALCULATIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if CALCULATE['result']:
        skill += ADD
        result = skill - skill_test
        CALCULATE['result'] = False

    if CALCULATE['bag']:
        chaos_bag_values = chaos_bag_for_probability(chaos_bag)

        f_succeed = lambda i: result_cycle(result, chaos_bag_values, i)
        list_for_table = [f_succeed(i) for i in succeed_or_fail_list if 'succeed' in i[1]]

        f_fail = lambda i: result_cycle(result, chaos_bag_values, i, skill_test)
        fail_list = [f_fail(i) for i in succeed_or_fail_list if 'fail' in i[1]]

        list_for_table.extend(fail_list)
        CALCULATE['bag'] = False


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PRINT A RESULT TABLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Head
    ADD_in_str = f' ({ADD} added)' if ADD else ''
    print(N_in_C(player))
    print(text_in_color(f'Skill is {skill} points{ADD_in_str}.'))
    print(f'Skill test is {skill_test}. Result is {result}')

    # result table
    table(list_for_table, result)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!MOD A RESULT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # PULL_TOKEN_to_RECALCULATE_FLAG
    PULL_TOKEN_to_RECALCULATE_FLAG = {'pull token': False, 'recalculate': False}

    PT_to_RC_q = {
        'to pull a chaos token': 'pull token',
        'to add points to a skill': 'recalculate'
    }

    # dialog interface
    PULL_TOKEN_to_RECALCULATE_FLAG = dialog_interface(PULL_TOKEN_to_RECALCULATE_FLAG, PT_to_RC_q, 'simple')

    if PULL_TOKEN_to_RECALCULATE_FLAG['recalculate']:

        dialog_dict = dialog_interface(CALCULATE, recalculate_questions, 'complex', player, recalculate_funcs)
        CALCULATE = dialog_dict['flags']

        # change a values
        if 'result' in dialog_dict:
            ADD = dialog_dict['result']

        if 'bag' in dialog_dict:
            chaos_bag = dialog_dict['bag']

    print()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PULL A TOKEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if PULL_TOKEN_to_RECALCULATE_FLAG['pull token']:
        # logs
        # list_by_0 = result_cycle(result, chaos_bag_values, (0, 'succeed by 0'))[0]
        # succeed_by_0 = [i[1] for i in list_by_0 if i[0] == str(result)]
        # write_a_log['checking'](player, skill, skill_test, succeed_by_0)

        bag_for_reveal = chaos_bag.copy()
        REVEAL_FLAG = True
        token_value = 0
        tokens = []

        while REVEAL_FLAG:

            token = choice(bag_for_reveal)
            token_name = f'"{token[0]}"'
            pull_token_value = token[1] if type(token[1]) == int else token[1][0]
            tokens.append(token_name)
            token_value += pull_token_value

            if type(token[1]) != int:
                bag_for_reveal.remove(token)
                print(N_in_C(f'{token_name} is pulled. Value is {token[1][0]}. You must reveal another token'))
# !!!!!!!!!!!!!!!!ДОБАВЬ ЗАДРЖКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            else:
                tokens_in_str = '=>'.join(tokens)
                is_plural = 'are' if len(tokens) > 1 else 'is'
                last_result = result + token_value
                REVEAL_FLAG = False

        # for especially tokens
        if "Auto-fail" in tokens_in_str:
            last_result = -skill_test
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. {player}`s skill is 0. Result is {last_result}'))
        elif "Elder Sign" in tokens_in_str and token_value > 50:
            last_result = skill
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. skill test is 0. Result is {last_result}'))
        else:
            print(N_in_C(f'{tokens_in_str} {is_plural} pulled. Value is {token_value}. Result is {last_result}'))

        # interpretation
        if last_result >= 0:
            total = f' succeed the skill test by {last_result}'
            print(N_in_C(player) + text_in_color(total, 'green'))
        else:
            total = f' fail the skill test by {abs(last_result)}'
            print(N_in_C(player) + text_in_color(total, 'red'))

        # logs
        # write_a_log['revealing'](player, tokens_in_str, token_value, last_result, total)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!reset to zero!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        CALCULATE = {key: True for key in CALCULATE}
        ADD = 0
        print('')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!RE-INPUT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        re_input_dialog = dialog_interface(INPUT_FLAGS, question_INPUT_FLAGS, 'complex')
        INPUT_FLAGS = re_input_dialog['flags']
        print('')
