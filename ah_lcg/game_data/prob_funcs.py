list_ = [-1, -2, -3, [-1, -2, -3], -4, -5, -5, [0], -2, -6, -2, -1, -99, [-1]]
index = list_.index([-1, -2, -3])
#print(index)



def done_percent(result, chaos_bag_values, num=0):
    done = [i+result for i in chaos_bag_values if i+result >= num]
    count_of_tokens = len(chaos_bag_values)
    success = len(done)
    done_percent = round((success/count_of_tokens) * 100)
    return done_percent


def success_counting_points_cycle(result, chaos_bag_values, num=0):
    add_done_percent_list = []
    dict_of_tokens = {}
    num_of_list = 1
    probability_list = []
    for i in chaos_bag_values: #исключаем списки. их будем считать отдельно
        if type(i) == list:
            dict_of_tokens['token'+str(num_of_list)] = i
            chaos_bag_values.remove(i)
            num_of_list += 1
    dict_of_tokens['bag'] = chaos_bag_values
    for add in range (1, 20): #counting points cycle
        new_result = result + add
        print(new_result)
        for key in dict_of_tokens:
            print(dict_of_tokens[key]) # печать списка
            new_done = [1 for i in dict_of_tokens[key] if i+new_result >= num]
            len_of_extention = 0
            if key == 'bag':
                new_done.extend(probability_list)
                len_of_extention = len(probability_list)
            print(new_done) # печать списка после проверки
            new_success = sum(new_done)
            print(new_success) # сумма после проверки
            limit_of_tokens = len(dict_of_tokens[key])+len_of_extention
            new_done_percent = round(new_success/limit_of_tokens, 2)
            if key != 'bag':
                probability_list.append(new_done_percent)
            print(new_done_percent) # процент успеха
        if new_done_percent > 0:
            add_done_percent_list.append((add, new_done_percent)) 
        if new_done_percent >= round((limit_of_tokens-1)/limit_of_tokens, 2):
            break
    return add_done_percent_list
            
### необходмо продумать... тут плавающая хрень, которая мешает. Нужен перевод и инт
                

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