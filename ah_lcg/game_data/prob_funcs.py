list_ = [-1, -2, [-3, -1], -4, -5, -5, 1, -2, -6, -2, -1, -99, 1]
#index = list_.index([-1, -2, -3])
#print(index)
#print(96%93)


def done_percent(result, chaos_bag_values, num=0):
    done = [1 for i in chaos_bag_values if i+result >= num]
    count_of_tokens = len(chaos_bag_values)
    success = sum(done)
    done_percent = success/count_of_tokens
    return done_percent

#print(done_percent(3, list_, 0))



def success_counting_points_cycle(result, chaos_bag_values, num=0):
    add_points_list = [] # здесь тоже можно что-нибудь дельное придумать. Облегчить код еси можно
    limit_of_bag = len(chaos_bag_values)
    dict_of_tokens = {}
    num_of_list = 1
    for i in chaos_bag_values: #исключаем списки. их будем считать отдельно
        if type(i) == list:
            dict_of_tokens['token'+str(num_of_list)] = i
            chaos_bag_values.remove(i)
            num_of_list += 1
    dict_of_tokens['bag'] = chaos_bag_values
    print(dict_of_tokens)
    for add in range (1,7): #counting points cycle
        new_result = result + add
        probability = 0
        for key in dict_of_tokens:
            limit_of_tokens = len(dict_of_tokens[key])
            if key != 'bag':
#                print(limit_of_bag)
                success = done_percent(new_result, dict_of_tokens[key], num) / (limit_of_bag)
            else: 
#                print(limit_of_tokens)
                success = done_percent(new_result, dict_of_tokens[key], num)
            success = int(success * 100)
            print(success)
            probability += success
        print(f'add {add}')
        print(f'% {probability}\n')
        if (probability >= 0 and add == 1) or probability > max_of_percent:
            add_points_list.append((add, probability))
            max_of_percent = probability
    return add_points_list
            
### необходмо продумать... не понимаю как сделать -99, ведь это не 100%!
                

    #print(dict_of_tokens)

        

def fail_counting_points_cycle(skill_test, result, chaos_bag_values, num=0):    
    chaos_bag_values.remove(-99)
    chaos_bag_values.append(-skill_test)
    for i in chaos_bag_values:
        if type(i) == list:
            i.remove(-99)
            i.append(-skill_test)
            # new_lose = [i+new_result for i in chaos_bag_values if i+new_result in num]
            # new_fail = len(new_lose)
            # new_fail_percent = round((new_fail/count_of_tokens) * 100)
            # if new_fail_percent > 0:
            #     new_fail_percent.append((add, new_done_percent)) 
            # if new_fail_percent >= round((count_of_tokens-1) / count_of_tokens * 100):
            #     return done_percent_list


#print(done_percent(0, [1,2,3,4,5], 2))
#print(f'If you add {add} point(s), done_procent is {new_done_percent}%')

print(success_counting_points_cycle(0, list_, 0))