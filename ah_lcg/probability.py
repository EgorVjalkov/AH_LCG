
from game_data.Roland_Banks import Roland_Banks
from game_data.scenario_token_value import *
#from game_data.Roland_Banks import enemies

#checking = [fight_action(), evade_action(), investigating(), myphos(), other()]


chaos_bag = night_of_the_zealot_normal_bag_keys
player = Roland_Banks
#enemy = ghoul

skill = player['combat']
check = int(input('skill check = '))
night_of_the_zealot_normal_bag['Elder_Sign'] = player['Elder_Sign_value']
#print(night_of_the_zealot_normal_bag)

def probability(skill, check, chaos_bag):
    result = skill - check
    print(f'result before chaos token is {result}')
    count_of_tokens  = len(chaos_bag)
    tokens_value = [night_of_the_zealot_normal_bag[i] for i in night_of_the_zealot_normal_bag_keys]
    print(tokens_value)
    done = [i for i in tokens_value if i+result >= 0]
    success = len(done)
    done_procent = round((success/count_of_tokens), 2) * 100
    print(f'done_procent is {done_procent}%')
    # adding point(s)
    if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
        for add in range (1, 20):
            new_result = result + add
            new_done = [i+new_result for i in tokens_value if i+new_result >= 0]
            new_success = len(new_done)
            new_done_percent = round((new_success/count_of_tokens) * 100)
            if new_done_percent > 0:
                print(f'if you add {add} point(s), done_procent is {new_done_percent}%')
            if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
                break
# Outdo 2 points percent
    if input('Press \'y\' and \'enter\' if you want to count 2 points passed percent. ') == 'y':
        increase_2 = [i for i in tokens_value if i+result >= 2]
        success2 = len(increase_2)
        increase_2_percent = round(success2/count_of_tokens * 100)
        print(f'2 points passed percent is {increase_2_percent}%')
    # adding point(s)        
        if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
            for add in range (1, 20):
                new_result = result + add
                new_done = [i+new_result for i in tokens_value if i+new_result >= 2]
                new_success = len(new_done)
                new_done_percent = round((new_success/count_of_tokens) * 100)
                if new_done_percent > 0:
                    print(f'if you add {add} point(s), 2 points passed percent is {new_done_percent}%')
                if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
                    break
# Outdo 4 points percent
    if input('Press \'y\' and \'enter\' if you want to count 4 points passed percent. ') == 'y':
        increase_4 = [i for i in tokens_value if i+result >= 4]
        success4 = len(increase_4)
        increase_4_percent = round(success4/count_of_tokens * 100)
        print(f'4 points passed percent is {increase_4_percent}%')
    # adding point(s)        
        if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
            for add in range (1, 20):
                new_result = result + add
                new_done = [i+new_result for i in tokens_value if i+new_result >= 4]
                new_success = len(new_done)
                new_done_percent = round((new_success/count_of_tokens) * 100)
                if new_done_percent > 0:
                    print(f'if you add {add} point(s), 4 points passed percent is {new_done_percent}%')
                if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
                    break                
# for crystal_pendulum
    if input('Press \'y\' and \'enter\' if you try to use the crystal pendulum. ') == 'y':
        add_point = input('Add any point(s) if you want to correct your skill ' )
        if not add_point.isdigit(): add_point = 0
        correction = int(add_point) + result
        abs_chaos_bag = [abs(i+correction) for i in tokens_value]
    #auto-fail correction
        abs_chaos_bag.remove(99-correction)
        abs_chaos_bag.append(check)
        print(abs_chaos_bag)
        for_crystal_pendulum = {}
        for i in abs_chaos_bag:
            for_crystal_pendulum[i] = abs_chaos_bag.count(i)
        max = 1
        for i in for_crystal_pendulum.items():
            if max < i[1]:
                max = i[1]
                num = i[0]
        probe = round(max/len(chaos_bag), 2) * 100
        print(f'number for crystal pendulum = {num}, probability is {probe}%')



probability(skill, check, chaos_bag)