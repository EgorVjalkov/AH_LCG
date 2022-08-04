def probability_of_list(result, choas_bag_for_mutations, num=(0,'succeed'), skill_test=0):
    print(num[0])
    mutated = list(map(lambda i: i + result, choas_bag_for_mutations)) # мутирование
    print(mutated)
    if 'fail' in num[1]: #переключатель функции
        mutated = list(map(lambda i: -skill_test if i < -80 else i, mutated)) # autofail corrrection
        if 'fail by or less' in num:
            filter_func = lambda i: i < 0 and i >= num[0]
        else: filter_func = lambda i: i <= num[0] and i > -30
    else:
        filter_func = lambda i: i >= num[0]
    filtered = list(filter(filter_func, mutated)) #фильтрация
    print(filtered)
    probability = len(filtered)/len(choas_bag_for_mutations)
    return round(probability, 4)


def counting_points_cycle(result, chaos_bag_values, num=(0,'succeed'), add_points=0, skill_test=0):
    choas_bag_for_mutations = []
    choas_bag_for_mutations.extend(chaos_bag_values) # чтобы не менялась реальная сумка
    add_points_list = []
    limit_of_bag = len(choas_bag_for_mutations)
    dict_of_tokens = {}
    num_of_list = 1
    for i in choas_bag_for_mutations: #исключаем списки. их будем считать отдельно
        if type(i) == list:
            dict_of_tokens['token'+str(num_of_list)] = i
            index_of_list = choas_bag_for_mutations.index(i)
            choas_bag_for_mutations.remove(i)
            choas_bag_for_mutations.insert(index_of_list, -50) #заглушка для удаленного списка
            num_of_list += 1
    dict_of_tokens['bag'] = choas_bag_for_mutations
    print(f'dict {dict_of_tokens}')
    for add in range (add_points+1): #counting points cycle
        new_result = result + add
        probability = 0
        for key in dict_of_tokens:
            if key != 'bag': #считаем вероятность для списков
                success = probability_of_list(new_result, dict_of_tokens[key], num, skill_test) / limit_of_bag
            else: #считаем вероятность для сумки (на месте списков заглушки)
                success = probability_of_list(new_result, dict_of_tokens[key], num, skill_test)
            success = round(success, 4) * 100
            print(success, '\n')
            probability += success
        print(probability)
        print('\n')
        probability = round(probability) #нормализуем вероятности
        add_points_list.append((add, probability))
    return add_points_list





#main func
def main():
    if __name__ == '__main__':
        from fast_token_value import chaos_bag_values_dict
        scenario = 'The Labirinths of Lunasy group A'
        player = 'Roland Banks'
        chaos_bag = chaos_bag_values_dict[scenario](player)
        print(chaos_bag) 
        args = (0, chaos_bag , (-2, 'fail by or less'), 2, 2)
        print(counting_points_cycle(*args))
#        print(list_)
#        args = (2, list_2, (-2, 'fail by or more'), 3) #для проверки функции вероятности
#        print(probability_of_list(*args))
#        print(list_)

main()
