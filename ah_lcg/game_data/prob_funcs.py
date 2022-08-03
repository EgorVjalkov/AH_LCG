list_ = [-1, -2, [-3, -1], -4, -5, [0, 0, -1], -5, 1, -2, [-99, -1, -3, -5], -6, -2, -1, -99, 1]
#index = list_.index([-1, -2, -3])
#print(index)

list_2 = [1, 1, 0, 0, -1, -1, -1, -2, -2, -3, -3, -1, -1, -2, -3, 3, -99]


def probability_of_list(result, chaos_bag_values, num=(0,'succeed')):
    if 'fail' in num[1]: #переключатель функции
        if 'fail by or less' in num:
            filter_func = lambda i: i+result < 0 and i+result >= num[0]# ato-fail!!!!!!!!!!!!!!!!
        else: filter_func = lambda i: i+result <= num[0]
    else:
        filter_func = lambda i: i+result >= num[0]
    filtered = list(filter(filter_func, chaos_bag_values))
    probability = len(filtered)/len(chaos_bag_values)
    return probability


def counting_points_cycle(result, chaos_bag_values, num=(0,'succeed'), add_points=0):
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
                success = probability_of_list(new_result, dict_of_tokens[key], num) / limit_of_bag
            else: #считаем вероятность для сумки (на месте списков заглушки)
                success = probability_of_list(new_result, dict_of_tokens[key], num)
            success *= 100
            probability += success
        probability = int(probability) #нормализуем вероятности
        if (probability >= 0 and add == 0) or probability > max_of_percent:
            add_points_list.append((add, probability))
            max_of_percent = probability #проверка на максимум. чтобы вовремя остановиться
    return add_points_list





#main func
def main():
    if __name__ == '__main__':
#        args = (0, list_2, (-2, 'fail by or more'))
        args = (0, list_)
#        print(probability_of_list(*args))
        print(counting_points_cycle(*args))

main()
