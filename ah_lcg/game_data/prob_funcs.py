list_ = [-1, -2, [-3, -1], -4, -5, [0, 0, -1], -5, 1, -2, [-99, -1, -3, -5], -6, -2, -1, -99, 1]
#index = list_.index([-1, -2, -3])
#print(index)

list_2 = [1, 1, 0, 0, -1, -1, -1, -2, -2, -3, -3, -1, -1, -2, -3, 3, -99]

def success_done_percent(result, chaos_bag_values, num=0):
    done = [1 for i in chaos_bag_values if i+result >= num]
    count_of_tokens = len(chaos_bag_values)
    success = sum(done)
    done_percent = success/count_of_tokens
    return done_percent

def fail_done_percent(result, chaos_bag_values, num=(-2, 'fail less')):
    if 'fail less' in num: 
        fail = [1 for i in chaos_bag_values if i+result < 0 and i+result >= num[0]]
    elif 'fail more' in num:
        fail = [1 for i in chaos_bag_values if i+result <= num[0]]
    count_of_tokens = len(chaos_bag_values)
    success = sum(fail)
    fail_percent = success/count_of_tokens
    return fail_percent

#print(success_done_percent(0, list_2, 0))


def counting_points_cycle(result, chaos_bag_values, num=0):
    if type(num) == tuple and 'fail' in num[1]: #переключатель функции
#        print(1)
        percent_func = fail_done_percent
    else: percent_func = success_done_percent
    add_points_list = []
    limit_of_bag = len(chaos_bag_values)
    dict_of_tokens = {}
    num_of_list = 1
    for i in chaos_bag_values: #исключаем списки. их будем считать отдельно
        if type(i) == list:
            dict_of_tokens['token'+str(num_of_list)] = i
            chaos_bag_values.remove(i)
            chaos_bag_values.append(-99) #заглушка для удаленного списка 
            num_of_list += 1
    dict_of_tokens['bag'] = chaos_bag_values
    for add in range (20): #counting points cycle
        new_result = result + add
        probability = 0
        for key in dict_of_tokens:
            if key != 'bag': #считаем вероятность для списков
                success = percent_func(new_result, dict_of_tokens[key], num) / (limit_of_bag)
            else: #считаем вероятность для сумки (на месте списков заглушки)
                success = percent_func(new_result, dict_of_tokens[key], num)
            success = success * 100
            probability += success
        probability = int(probability) #нормализуем вероятности
        if (probability >= 0 and add == 0) or probability > max_of_percent:
            add_points_list.append((add, probability))
            max_of_percent = probability #проверка на максимум. чтобы вовремя остановиться
    return add_points_list


<<<<<<< HEAD
print(counting_points_cycle(0, list_, (-2, 'fail more')))
=======
print(counting_points_cycle(-4, list_, (-2, 'fail more')))
>>>>>>> 342b2b4f4fe7aabe05a458a0004b1addaff82608
