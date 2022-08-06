def probability_of_list(result, choas_bag_for_mutations, num=(0,'succeed'), skill_test=0):
#    print(num[0])
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
    return len(filtered)


def counting_points_cycle(result, dict_of_tokens, num=(0,'succeed'), add_points=0, skill_test=0):
    add_points_list = []
    divider = dict_of_tokens.pop('bag divider')
    for add in range (add_points+1): #counting points cycle
        new_result = result + add
        probability = 0
        for key in dict_of_tokens:
            if key != 'bag': #считаем вероятность для списков
                success = probability_of_list(new_result, dict_of_tokens[key], num, skill_test) / pow(divider, 2)
            else: #считаем вероятность для сумки (на месте списков заглушки)
                success = probability_of_list(new_result, dict_of_tokens[key], num, skill_test) / divider
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
        from fast_token_value import keys_dict, chaos_bag_for_pulling, chaos_bag_for_probability
        scenario = 'The Labirinths of Lunasy standard group A'
        player = 'Roland Banks'
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        next_bag = chaos_bag_for_probability(chaos_bag)
#        print(next_bag) 
        args = (0, next_bag)
        print(counting_points_cycle(*args))
#        print(list_)
#        args = (2, list_2, (-2, 'fail by or more'), 3) #для проверки функции вероятности
#        print(probability_of_list(*args))
#        print(list_)

main()
