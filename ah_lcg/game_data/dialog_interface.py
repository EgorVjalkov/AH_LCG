from input_checking import input_checking as ICh
from colored_keywords import names_in_color as N_in_C


dialog_interface_dict = {
        'adding': 'to add any points',
        '2': 'to succeed a skill test by 2 or more',
        '3': 'to succeed a skill test by 3 or more',
        '4': 'to succeed a skill test by 4 or more',
        '-2': 'to fail a skill test by 2 or less',
        'pass': 'to pull a token' }

def dialog_interface(result, player):
    add_skill = 0
    while True:
        result += add_skill
        print(f'result = {result}')
        for i, el in enumerate(dialog_interface_dict.values()):
            print(N_in_C(f'press "{i+1}" and "enter" - {el}'))
        q = ': '
        answer = ICh(': ', ('1','2','3','4','5','6'))
        if answer == '6':
            return result
        if answer == '1':
            q2 = N_in_C(f'How many points does {player} need to? Press "num" and "enter" ')
            add_skill = ICh(q2, 'num')


print(dialog_interface(5, 'Egorok'))