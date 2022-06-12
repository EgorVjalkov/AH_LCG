from game_data.scenario_token_value import night_of_the_zealot_normal as NZ_norm 


skill = int(input('Investigator`s skill = '))
check = int(input('skill check = '))
chaos_bag = NZ_norm


def probability(skill, check, chaos_bag):
    result = skill - check
    print(f'result before chaos token is {result}')
    count_of_tokens  = len(chaos_bag)
    done = [i for i in chaos_bag if i+result >= 0]
    success = len(done)
    done_procent = round((success/count_of_tokens), 2) * 100
    print(f'done_procent is {done_procent}%')
    # adding point(s)
    if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
        for add in range (1, 20):
            new_result = result + add
            new_done = [i+new_result for i in chaos_bag if i+new_result >= 0]
            new_success = len(new_done)
            new_done_percent = round((new_success/count_of_tokens) * 100)
            print(f'if you add {add} point(s), done_procent is {new_done_percent}%')
            if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
                break
# Outdo 2 points percent
    if input('Press \'y\' and \'enter\' if you want to count 2 points passed percent. ') == 'y':
        increase_2 = [i for i in chaos_bag if i+result >= 2]
        success2 = len(increase_2)
        increase_2_percent = round(success2/count_of_tokens * 100)
        print(f'2 points passed percent is {increase_2_percent}%')
    # adding point(s)        
        if input('Press \'y\' and \'enter\' if you want to add any point(s). ') == 'y':
            for add in range (1, 20):
                new_result = result + add
                new_done = [i+new_result for i in chaos_bag if i+new_result >= 2]
                new_success = len(new_done)
                new_done_percent = round((new_success/count_of_tokens) * 100)
                print(f'if you add {add} point(s), 2 points passed percent is {new_done_percent}%')
                if new_done_percent >= round(((count_of_tokens-1) / count_of_tokens) * 100):
                    break
# for crystal_pendulum
    if input('Press \'y\' and \'enter\' if you try to use the crystal pendulum. ') == 'y':
        add_point = input('Add any point(s) if you want to correct your skill ' )
        if not add_point.isdigit(): add_point = 0
        correction = int(add_point) + result
        abs_chaos_bag = [abs(i+correction) for i in chaos_bag]
    #auto-fail correction
        abs_chaos_bag.remove(99+correction)
        abs_chaos_bag.append(check)
        print(abs_chaos_bag)
        for_crystal_pendulum = []
        for i in range (min(abs_chaos_bag), max(abs_chaos_bag)+1):
            for_crystal_pendulum.append(i)
            for_crystal_pendulum.append(abs_chaos_bag.count(i))
        print(for_crystal_pendulum)
        print(for_crystal_pendulum[1::2])
        print(max(for_crystal_pendulum[1::2]))
        tokens = max(for_crystal_pendulum[1::2])
        num = for_crystal_pendulum[for_crystal_pendulum.index(tokens)-1]
        probe = round(max(for_crystal_pendulum[1::2])/len(abs_chaos_bag), 2) * 100
        print(f'number for crystal pendulum = {num}, probability is {probe}%')



probability(skill, check, chaos_bag)







#skull_token = int(input('skull token = '))
#cultist_token = int(input('cultist token = '))
#tablet_token = int(input('tablet token = '))
#Elder_Thing_token = input('Elder Thing token = ')
#Elder_Sign_token = int(input('Elder Sign token = '))
#Auto_fail_token = - check
#if not Elder_Thing_token:
#    chaos_bag = [
#        1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_token, skull_token, 
#        cultist_token, tablet_token, Auto_fail_token, Elder_Sign_token
#        ]
#else: chaos_bag = [
#        1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_token, skull_token, 
#        cultist_token, tablet_token, Auto_fail_token, Elder_Sign_token, int(Elder_Thing_token)
#        ]
