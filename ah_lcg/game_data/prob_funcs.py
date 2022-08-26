# функция подсчета вероятности в списке
def probability_of_list(result, choas_bag_for_mutations, num=(0,'succeed'), skill_test=0):
    #print(result)
    mutated = list(map(lambda i: i + result, choas_bag_for_mutations)) # мутирование
    #print(mutated)
    if 'fail' in num[1]: #переключатель функции
        mutated = list(map(lambda i: -skill_test if i < -80 else i, mutated)) # autofail corrrection
        if 'less' in num[1]:
            filter_func = lambda i: i < 0 and i >= num[0]
        else: filter_func = lambda i: i <= num[0] and i > -30
    else:
        filter_func = lambda i: i >= num[0]
    filtered = list(filter(filter_func, mutated)) #фильтрация
    #print(filtered)
    return len(filtered)

# функция, которая готовит списки для probability_of_list из словаря. Гоняет их в цикле набора очков
def counting_points_cycle(result, dict_of_tokens, add_points=0, num=(0,'succeed'), skill_test=0):
    add_points_list = []
    divider = dict_of_tokens['bag divider']
    dict_of_tokens_for_mutation = {key: dict_of_tokens[key] for key in dict_of_tokens if key != 'bag divider'}
    print(dict_of_tokens_for_mutation)
    for add in range (add_points+1): #counting points cycle
        new_result = result + add
        probability = 0
        for key in dict_of_tokens_for_mutation:
            if key != 'bag': #считаем вероятность для списков
                success = probability_of_list(new_result, dict_of_tokens_for_mutation[key], num, skill_test) / pow(divider, 2)
            else: #считаем вероятность для сумки
                success = probability_of_list(new_result, dict_of_tokens_for_mutation[key], num, skill_test) / divider
            success = round(success, 4) * 100
#            print(success, '\n')
            probability += success
#        print(probability)
        probability = round(probability) #нормализуем вероятности
        add_points_list.append((add, probability))
    return add_points_list


def result_normalize(result):
    result_list = list(i for i in range(-3, 11))
    if result not in result_list:
        start = result - 1
        result_list = list(i for i in range(start, start+14))
    return result_list


# функция, которая готовит списки для probability_of_list из словаря. Гоняет их в цикле results
def result_cycle(result, dict_of_tokens, num=(0, 'succeed by or more'), skill_test=0):
    add_points_list = []
    divider = dict_of_tokens['bag divider']
    dict_of_tokens_for_mutation = {key: dict_of_tokens[key] for key in dict_of_tokens if key != 'bag divider'}
    result_list = result_normalize(result)
#    print(dict_of_tokens_for_mutation)
    for i in result_list: #counting points cycle
        probability = 0
        for key in dict_of_tokens_for_mutation:
            if key != 'bag': #считаем вероятность для списков
                success = probability_of_list(i, dict_of_tokens_for_mutation[key], num, skill_test) / pow(divider, 2)
            else: #считаем вероятность для сумки
                success = probability_of_list(i, dict_of_tokens_for_mutation[key], num, skill_test) / divider
            success = round(success, 4) * 100
#            print(success, '\n')
            probability += success
#        print(probability)
        probability = str(round(probability)) #нормализуем вероятности
        add_points_list.append((str(i), probability))
    return add_points_list, num


#main func
def main():
    if __name__ == '__main__':
        from fast_token_value import keys_dict, chaos_bag_for_pulling, chaos_bag_for_probability
        scenario = 'The Labyrinths of Lunasy standard group A'
        player = 'Roland Banks'
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        next_bag = chaos_bag_for_probability(chaos_bag)
        print(result_cycle(-6, next_bag))

main()
