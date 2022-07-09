# похоже надо делать 3 сумки: одну с ключами, 2 для вероятности, 3 для функций
#значения жетонов
#from investigators import Roland_Banks_Elder_Sign
from colored_keywords import colored_keywords as CKW
from random import choice


The_gathering_normal_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Sign', 'Auto-fail']
The_Devouver_Below_normal_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Thing', 'Elder Sign', 'Auto-fail']

#skull
def skull_value(scenario):
    if scenario == 'The Gathering normal':
        return -int(input(CKW('The number of Ghoul enemies at your location is ')))
    elif scenario == 'The Midnight Masks normal':
        return -int(input(CKW('The highest number of doom on a Cultist enemy in play is: ')))
    elif scenario == 'The Devourer Below normal': 
        return -int(input(CKW('The number of Monster enemies in play is ')))

def skull_failure(scenario):
    pass


#cultist
def cultist_value(scenario):
    if scenario == 'The Gathering normal':
        return -1
    elif scenario == 'The Midnight Masks normal':
        return (-2, CKW('Place 1 doom on the nearest Cultist enemy'))
    elif scenario == 'The Devourer Below normal': 
        return (-2, CKW('Place 1 doom on the nearest enemy'))

def cultist_failure(scenario):
    if scenario == 'The Gathering normal':
        return CKW('take 1 horror')


#tablet
def tablet_value(scenario):
    if scenario == 'The Gathering normal':
        if input(CKW('Press \'y\' and \'enter\' if there is a Ghoul enemy at your location ')) == 'y':
            return (-2, CKW('take 1 damage'))
        else: return -2
    elif scenario == 'The Midnight Masks normal':
        return -3
    elif scenario == 'The Devourer Below normal': 
        if input(CKW('Press \'y\' and \'enter\' if there is a Monster enemy at your location ')) == 'y':
            return (-3, CKW('take 1 damage'))
        else: return -3

def tablet_failure(scenario):
    if scenario == 'The Midnight Masks normal':
        return CKW('Place 1 of your clues on your location.')

Token_symbol_value = {
    'skull': skull_value, 'cultist': cultist_value, 'tablet': tablet_value, 
     'Elder Sign': 'Elder_Sign_value'}

#Elder Thing
def Elder_Thing_value(scenario):
    if scenario == 'The Devourer Below normal': 
        if input(CKW('Press \'y\' and \'enter\', if there is an Ancient One enemy in play ')) == 'y':
            print('You must reveal another token')
            The_Devouver_Below_normal_keys.remove('Elder Thing')
            token = choice(The_Devouver_Below_normal_keys)
            print(f'You pulled {CKW(token)}')
            if token in Token_symbol_value:
                token_value = Token_symbol_value[token](scenario)
                if type(token_value) == 'tuple':
                    return -5, token_value[1]
                else: return -5
            else: return -5   
        else: return -5

def Elder_Thing_failure(scenario):
    pass


#print(skull_value('The Devourer Below normal'))
print(Elder_Thing_value('The Devourer Below normal'))

Token_symbol_value = {
    'skull': skull_value, 'cultist': cultist_value, 'tablet': tablet_value, 
    'Elder Thing': Elder_Thing_value, 'Elder Sign': 'Elder_Sign_value'}



# #список с ключами от словаря


#для тестов
only_auto_fail_bag = {'Auto-fail': -99}
only_auto_fail_bag_keys = ['Auto-fail']
only_Elder_Sign_bag = {'Elder Sign': 1}
only_Elder_Sign_bag_keys = ['Elder Sign']

#print(night_of_the_zealot_normal_bag)

def main():
    if __name__ == '__main__':
        main()