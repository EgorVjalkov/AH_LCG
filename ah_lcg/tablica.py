from game_data.prob_funcs import probability_of_list, result_cycle
from game_data.fast_token_value import keys_dict, players, chaos_bag_for_probability, chaos_bag_for_pulling
from game_data.colored_keywords import text_in_color, colored_points_dict, color
from colorama import Style


# ячейка


def colored_cell(points, percent, result):

    for i in points, percent:
        color_key = tuple(key for key in colored_points_dict if colored_points_dict[key] > percent)[0]
        if len(i) == 1:
            i = f'| {str(i)} |'
        elif len(i) == 2:
            i = f'| {str(i)}|'
        else:
            i = f'|{str(i)}|'

    # color_key = tuple(key for key in colored_points_dict if result_points_dict[key] > percent)[0]
    # colored_percent = color[color_key] + (str(percent) + '%') + Style.RESET_ALL
    # colored_points = color[color_key] + str(points) + Style.RESET_ALL
    print(points, percent, )
# полностью меняем колоред пойнтс будем вшивать в фунецию ячейки

print(colored_cell(4, 75, 4))


# печатает в терминале таблицу цветную
def table(tupled_list):
    for el in tupled_list:
        list_of_probability = el[0]
        result_of_skill_test = el[1]
        for i in list_of_probability:
            result_percent_in_color = [colored_points(int(i[0]), int(i[1])) for i in list_of_probability]
        if 0 in result_of_skill_test:
            head_list = [cell(i[0]) for i in result_percent_in_color]
            head = ''.join(head_list)
            print('-' * 90)
            head = text_in_color('result              ', 'fat') + head
            print(head)
            print('-' * 90)
        cells_list = [cell(i[1]) for i in result_percent_in_color]
        cells = ''.join(cells_list)
        if 'succeed' in result_of_skill_test[1]:
            column = text_in_color(result_of_skill_test[1], 'green')
        else:                
            column = text_in_color(result_of_skill_test[1], 'red') + '   '
        print(column + cells)
        print('-' * 90)
        
        
scenario = 'The Gathering standard'
player = 'Roland Banks'


result_list = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


succeed_or_fail_list = []
for i in range(0, 5):
    num = (i, f'succeed by {i} or more')
    succeed_or_fail_list.append(num)
succeed_or_fail_list.append((-2, 'fail by 2 or less'))
succeed_or_fail_list.append((-2, 'fail by 2 or more'))
# print(succeed_or_fail_list)


skill = int(input('Skill? '))
skill_test = int(input('Skill_test? '))
result = skill - skill_test
chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
chaos_bag_values = chaos_bag_for_probability(chaos_bag)
# print(succeed_or_fail_list)
succeed_or_fail_result_percent_tuple_list = [
    result_cycle(result_list, chaos_bag_values, i) for i in succeed_or_fail_list if 'succeed' in i[1]
    ]
fail_result_percent_tuple_list = [
    result_cycle(result_list, chaos_bag_values, i, skill_test) for i in succeed_or_fail_list if 'fail' in i[1]
    ]
succeed_or_fail_result_percent_tuple_list.extend(fail_result_percent_tuple_list)
# print(succeed_or_fail_result_percent_tuple_list)
table(succeed_or_fail_result_percent_tuple_list)
        
