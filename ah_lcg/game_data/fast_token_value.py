from colored_keywords import colored_keywords as CKW
#from game_data.colored_keywords import colored_keywords as CKW
from random import choice
#ключи к сумкам

The_gathering_normal_keys = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign']

The_Devouver_Below_normal_keys = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Thing', 'Auto-fail', 'Elder Sign']

keys = {'The Gathering normal': The_gathering_normal_keys,
'The Midnight Masks normal': The_gathering_normal_keys,
'The Devourer Below normal': The_Devouver_Below_normal_keys}

players = ('Roland Banks', 'Daisy Walker', '"Skids" O`Toole', 'Agnes Baker', 'Wendy Adams')


#Символы

#Auto-fail
def Auto_fail(scenario=0, player=0):
    return -99

#skull
def skull_value(scenario, player=0):
    while True:
        if scenario == 'The Gathering normal':
            modificator = (input(CKW('The number of Ghoul enemies at your location is ')))
        elif scenario == 'The Midnight Masks normal':
            modificator = (input(CKW('The highest number of doom on a Cultist enemy in play is: ')))
        elif scenario == 'The Devourer Below normal': 
            modificator = (input(CKW('The number of Monster enemies in play is ')))
        # for new scenario
        if modificator.isdigit(): # проверка ввода
                break
        print('Input Error')
    skull_value = -int(modificator)
    return skull_value

#cultist
def cultist_value(scenario, player=0):
    if scenario == 'The Gathering normal':
        return -1
    elif scenario == 'The Midnight Masks normal':
        return -2
    elif scenario == 'The Devourer Below normal': 
        return -2

#tablet
def tablet_value(scenario, player=0):
    if scenario == 'The Gathering normal':
        return -2
    elif scenario == 'The Midnight Masks normal':
        return -3
    elif scenario == 'The Devourer Below normal': 
        return -3

#Elder_Sign for Core Set investigators
def Elder_Sign_value(scenario, player):
    investigators_in_str = ', '.join(players)
    while True: # проверка ввода
        if player in players:
            break
        print(f'Input Error. Incorrect name. Investigators are {investigators_in_str}' )
        player = input('Player is ')
    if player == 'Roland Banks':
        while True: # проверка ввода
            Elder_Sign = input(CKW('How many clues are at your location? Press a \'num\' and \'enter\' '))
            if Elder_Sign.isdigit(): 
                break
            print('Input Error')
    if player == '"Skids" O`Toole':
        Elder_Sign = 2
    if player == 'Daisy Walker':
        Elder_Sign = 0
    if player == 'Agnes Baker':
        while True: # проверка ввода
            Elder_Sign = input(CKW('How many horror are on Agnes Baker? Press a \'num\' and \'enter\' '))
            if Elder_Sign.isdigit(): 
                break
            print('Input Error')
    if player == 'Wendy Adams':
        while True: # проверка ввода
            Elder_Sign = input(CKW('Does Wendy`s amulet in play?. Press "y" or "n" and "enter" '))
            if Elder_Sign == 'y' or Elder_Sign == 'n': 
                break
            print('Input Error')
        if Elder_Sign == 'y': Elder_Sign = 99
        else: Elder_Sign = 0
    return int(Elder_Sign)

#print(Elder_Sign_value('The Gathering normal', 'Wendy Adams'))

#Elder Thing
def Elder_Thing_value(scenario, player=0):
    token_symbol_value_for_Elder_Thing = {
    'skull': skull_value, 'cultist': cultist_value, 'tablet': tablet_value, 
     'Elder Sign': Elder_Sign_value}
    if scenario == 'The Devourer Below normal': 
        if input(CKW('Press \'y\' and \'enter\', if there is an Ancient One enemy in play ')) == 'y':
            print('You must reveal another token')
            The_Devouver_Below_normal_keys.remove('Elder Thing')
            token = choice(The_Devouver_Below_normal_keys)
            print(f'You pulled a {CKW(token)}')
            if token in token_symbol_value_for_Elder_Thing:
                token_value = token_symbol_value_for_Elder_Thing[token](scenario)
                print(CKW(f'The {token} value is {token_value}.'))
                return -5 + token_value
            else: return -5 + int(token)   
        else: return -5

#print(Elder_Thing_value('The Devourer Below normal'))

token_symbol_value = {
    'skull': skull_value, 'cultist': cultist_value, 'tablet': tablet_value, 
    'Elder Thing': Elder_Thing_value, 'Elder Sign': Elder_Sign_value, 'Auto-fail': Auto_fail}

def chaos_bag_values(scenario, player):
    scenario_keys = keys[scenario]
    scenario_values = []
    i = 0
    while i < len(scenario_keys):
        el = scenario_keys[i]
        if type(el) == int:
            scenario_values.append(el)
            i += 1
        else:
            if el == 'Elder Thing': i += 1
            else:
                value = token_symbol_value[el](scenario, player)
                values = [value] * scenario_keys.count(el)
                scenario_values.extend(values)
                i += scenario_keys.count(el)
    if 'Elder Thing' in scenario_keys:
        Elder_Thing = [i-5 for i in scenario_values]
        scenario_values.append(Elder_Thing)
    return scenario_values

#нужно разобраться со значком старцев, т.к. не понятно когда его вызывать, и куда деть вероятность, \
# как ее считать по закону вероятностей (сложение вероятностей или типа того)

print(chaos_bag_values('The Devourer Below normal', 'Roland Banks'))