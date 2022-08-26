from random import choice
from fast_token_value import chaos_bag_for_pulling, keys_dict


def result_normalize(result):
    result_list = list(i for i in range(-3, 11))
    if result not in result_list:
        start = result - 1
        result_list = list(i for i in range(start, start+14))
    return result_list


print(result_normalize(-6))
