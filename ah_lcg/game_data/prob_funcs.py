list_ = [-1, -2, [-3, -1], -4, -5, [0, 0, -1], -5, 1, -2, [-99, -1, -3, -5], -6, -2, -1, -99, 1]
#index = list_.index([-1, -2, -3])
#print(index)

list_2 = [1, 1, 0, 0, -1, -1, -1, -2, -2, -3, -3, -1, -1, -2, -3, 3, -99]

def success_done_percent(result, chaos_bag_values, num=0):
    done = lambda i: 1 if i+result >= num else 0
    success = sum([done(i) for i in chaos_bag_values])
    done_percent = success/len(chaos_bag_values)
    return done_percent


def fail_done_percent(result, chaos_bag_values, num=(-2, 'fail by or less')):
    if 'fail by or less' in num:
        done = lambda i: 1 if i+result < 0 and i+result >= num[0] else 0
    else: done = lambda i: 1 if i+result <= num[0] else 0
    fail = sum([done(i) for i in chaos_bag_values])
    fail_percent = fail/len(chaos_bag_values)
    return fail_percent

args = (0, list_2, (-2, 'fail by or more'))
print(fail_done_percent(*args))


def counting_points_cycle(result, chaos_bag_values, num=0, add_points=1):
    if type(num) == tuple and 'fail' in num[1]: #переключатель функции
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
    for add in range (add_points+1): #counting points cycle
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

args = (0, list_, 0)
print(counting_points_cycle(0, list_, 0, 3))
