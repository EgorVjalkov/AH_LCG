from ah_lcg.game_data.prob_funcs import probability_of_list, result_cycle
from ah_lcg.game_data.fast_token_value import keys_dict, chaos_bag_for_probability, chaos_bag_for_pulling
from ah_lcg.game_data.colored_keywords import text_in_color, colored_points_dict, result_points_dict, color
from colorama import Style


# ячейка
def colored_cell(points, percent, result):
    if points == result:
        color_key = tuple(key for key in result_points_dict if result_points_dict[key] >= percent)[0]
        line_format = color[color_key] + ' ' + Style.RESET_ALL
    else:
        color_key = tuple(key for key in colored_points_dict if colored_points_dict[key] >= percent)[0]
        line_format = Style.DIM + '|' + Style.RESET_ALL
    colored_cell = []
    for el in [str(points), str(percent)+'%']:
        if len(el) == 1:
            el = line_format + (color[color_key] + (' '+str(el)+' ') + Style.RESET_ALL) + line_format
        elif len(el) == 2:
            el = line_format + (color[color_key] + (' '+str(el)) + Style.RESET_ALL) + line_format
        elif len(el) == 3:
            el = line_format + (color[color_key] + (str(el)) + Style.RESET_ALL) + line_format
        else:
            el = (color[color_key] + (str(el)) + Style.RESET_ALL) + line_format
        colored_cell.append(el)
    return colored_cell


# печатает в терминале таблицу цветную
def table(tupled_list, result=0):
    for el in tupled_list:
        list_of_probability = el[0]
        result_of_skill_test = el[1]
        for el in list_of_probability:
            result_percent_in_color = [colored_cell(int(i[0]), int(i[1]), result) for i in list_of_probability]
        if 0 in result_of_skill_test:
            head_list = [i[0] for i in result_percent_in_color]
            head = ''.join(head_list)
            print('-' * 90)
            head = text_in_color('result              ', 'fat') + head
            print(head)
            print('-' * 90)
        cells_list = [i[1] for i in result_percent_in_color]
        cells = ''.join(cells_list)
        if 'succeed' in result_of_skill_test[1]:
            column = text_in_color(result_of_skill_test[1], 'green')
        else:                
            column = text_in_color(result_of_skill_test[1], 'red') + '   '
        print(column + cells)
        print('-' * 90)
        

succeed_or_fail_list = []
for i in range(0, 5):
    num = (i, f'succeed by {i} or more')
    succeed_or_fail_list.append(num)
succeed_or_fail_list.append((-2, 'fail by 2 or less'))
succeed_or_fail_list.append((-2, 'fail by 2 or more'))
# print(succeed_or_fail_list)



def main():
    if __name__ == '__main__':
        scenario = 'The Midnight Masks standard'
        player = 'Agnes Baker'
        skill = int(input('Skill: '))
        skill_test = int(input('Skill test: '))
        result = skill - skill_test
        print(f'Result is {result}')
        chaos_bag = chaos_bag_for_pulling(keys_dict, scenario, player)
        chaos_bag_values = chaos_bag_for_probability(chaos_bag)
        # print(succeed_or_fail_list)
        succeed_or_fail_result_percent_tuple_list = [
            result_cycle(chaos_bag_values, i) for i in succeed_or_fail_list if 'succeed' in i[1]
            ]
        fail_result_percent_tuple_list = [
            result_cycle(chaos_bag_values, i, skill_test) for i in succeed_or_fail_list if 'fail' in i[1]
            ]
        succeed_or_fail_result_percent_tuple_list.extend(fail_result_percent_tuple_list)
        # print(succeed_or_fail_result_percent_tuple_list)
        table(succeed_or_fail_result_percent_tuple_list, result)
        

main()
