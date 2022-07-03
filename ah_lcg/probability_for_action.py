from game_data.colored_keywords import colored_keywords as CKW # цветные имена
from random import choice
#from game_data.scenario_token_value import * #исключительно для внутреннего теста

#добавил проверку на максимум, когда добавлять очки не нужно

def short_probability(result, chaos_bag, chaos_bag_keys):
    count_of_tokens  = len(chaos_bag_keys)
    tokens_value = [chaos_bag[i] for i in chaos_bag_keys]
#    print(tokens_value)
    done = [i for i in tokens_value if i+result >= 0]
    success = len(done)
    done_procent = round((success/count_of_tokens) * 100)
    if done_procent >= round((count_of_tokens-1) / count_of_tokens * 100):
        print(f'done_procent is {done_procent}%! You not need any points!')
    else: 
        print(f'done_procent is {done_procent}%')
        #adding points
        if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
            for add in range (1, 20):
                new_result = result + add
                new_done = [i+new_result for i in tokens_value if i+new_result >= 0]
                new_success = len(new_done)
                new_done_percent = round((new_success/count_of_tokens) * 100)
                if new_done_percent > 0:
                    print(f'If you add {add} point(s), done_procent is {new_done_percent}%')
                if new_done_percent >= round((count_of_tokens-1) / count_of_tokens * 100):
                    break

#short_probability(2, night_of_the_zealot_normal_bag, night_of_the_zealot_normal_bag_keys)

def pull_a_token(chaos_bag, chaos_bag_keys, result, check):
    token = choice(chaos_bag_keys)
    if token == 'Auto-fail':
        last_result = -check
        print(CKW(f'You pulled Auto-fail! Result is {last_result}'))
    else:
        last_result = result + chaos_bag[token]
        if not token.isalpha():
            print(CKW(f'You pulled {token}. Result is {last_result}'))
        else:
            print(CKW(f'You pulled {token}. Value is {chaos_bag[token]}. Result is {last_result}'))
    return last_result

#pull_a_token(night_of_the_zealot_normal_bag, night_of_the_zealot_normal_bag_keys, 5, 2)


