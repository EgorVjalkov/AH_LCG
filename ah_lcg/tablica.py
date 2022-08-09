from game_data.prob_funcs import probability_of_list
from game_data.fast_token_value import keys_dict, players, chaos_bag_for_probability, chaos_bag_for_pulling
from game_data.colored_keywords import colored_points, text_in_color


def result_cycle(results, dict_of_tokens, num=(0,'succeed by or more'), skill_test=0):
    add_points_list = []
    divider = dict_of_tokens['bag divider']
    dict_of_tokens_for_mutation = {key: dict_of_tokens[key] for key in dict_of_tokens if key != 'bag divider'}
#    print(dict_of_tokens_for_mutation)
    for i in results: #counting points cycle
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


succeed_or_fail_list = []
for i in range(0, 5):
    num = (i, f'succeed by {i} or more')
    succeed_or_fail_list.append(num)
succeed_or_fail_list.append((-2, 'fail by 2 or less'))
succeed_or_fail_list.append((-2, 'fail by 2 or more'))
print(succeed_or_fail_list)


def cell(value):
    if len(value) == 10:
        return f'| {str(value)} |'
    elif len(value) == 11:
        return f'| {str(value)}|'
    else:
        return f'|{str(value)}|'


def table(tupled_list):
    for el in tupled_list:
        list_of_probability = el[0]
        result_of_skill_test = el[1]
        for i in list_of_probability:
            result_percent_in_color = [colored_points(int(i[0]), int(i[1])) for i in list_of_probability]
        if 0 in result_of_skill_test:
            head_list = [cell(i[0]) for i in result_percent_in_color]
            head = ''.join(head_list)
            print('-' * (len(tupled_list)* 10 +20))
            head = text_in_color('result              ', 'fat') + head
            print(head)
            print('-' * (len(tupled_list)* 10 +20))
        cells_list = [cell(i[1]) for i in result_percent_in_color]
        cells = ''.join(cells_list)
        if 'succeed' in result_of_skill_test[1]:
            column = text_in_color(result_of_skill_test[1], 'green' )
        else:                
            column = text_in_color(result_of_skill_test[1], 'red' ) + '   '
        print(column + cells)
        print('-' * (len(tupled_list)* 10 +20))

#    coloring = zip(head_list, cells_list_by_0)
#    coloring = [colored_points(int(i[0]), int(i[1])) for i in coloring]
#    print(coloring)
    
    
    
    # cells = ''.join(cells_list_by_0)
    # print(text_in_color('succeed', 'green' )+ cells)
    # print('-' * (len(tupled_list) * 5 + 21))


scenario = 'The Labyrinths of Lunasy standard group B'
player = 'Roland Banks'

result_list = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

skill_test = -int(input('Skill_test? '))
chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
chaos_bag_values = chaos_bag_for_probability(chaos_bag)
#print(succeed_or_fail_list)
succeed_or_fail_result_percent_tuple_list = [
    result_cycle(result_list, chaos_bag_values, i) for i in succeed_or_fail_list if 'succeed' in i[1]
    ]
fail_result_percent_tuple_list = [
    result_cycle(result_list, chaos_bag_values, i, skill_test) for i in succeed_or_fail_list if 'fail' in i[1]
    ]
succeed_or_fail_result_percent_tuple_list.extend(fail_result_percent_tuple_list)
#print(succeed_or_fail_result_percent_tuple_list)
table(succeed_or_fail_result_percent_tuple_list)
        
