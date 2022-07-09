from colored_keywords import colored_keywords as CKW
from random import choice
#ключи к сумкам

The_gathering_normal_keys = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign'] #убрал пока значок древних

The_Devouver_Below_normal_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'ElderThing', 'Elder Sign', 'Autofail']

keys = {'The Gathering normal': The_gathering_normal_keys, 
'The Devouver Below normal': The_Devouver_Below_normal_keys}

players = ('Roland Banks')


#Символы

def Auto_fail(scenario=0, player=0):
    return -99

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

# Elder Sign ПОЧЕМУТО НОНЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Elder_Sign_value(scenario, player):
    investigators_in_str = ', '.join(players)
    while True: # проверка ввода
        if player in players:
            break
        print(f'Input Error. Incorrect name. Investigators are {investigators_in_str}' )
        player = input('Player is ')
    if player == 'Roland Banks':
        while True: # проверка ввода
            Elder_Sign = input(CKW('does any clue at your location? Press a \'num\' and \'enter\' '))
            if Elder_Sign.isdigit(): 
                break
            print('Input Error')
        return int(Elder_Sign)

print(Elder_Sign_value('The Gathering normal', 'Roland Bank'))

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

def create_a_chaos_bag(scenario, player):
    scenario_keys = keys[scenario]
    scenario_values = []
    for i in scenario_keys:
        if type(i) == int:
            scenario_values.append(i)
        else:
            value = token_symbol_value[i](scenario, player)
            scenario_values.append(value)   
    return scenario_values



#print(create_a_chaos_bag('The Gathering normal', 'Roland Bank'))