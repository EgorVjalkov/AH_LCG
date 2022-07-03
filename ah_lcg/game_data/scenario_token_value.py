# похоже надо делать 3 сумки: одну с ключами, 2 для вероятности, 3 для функций
#значения жетонов

def skull_value(scenario):
    if scenario == 'Night of the Zealot normal':
        return int(input('Count of ghouls at your location: '))

def skull_falure(scenario, enemy):
    if scenario == 'Night of the Zealot normal':
        if enemy['Class'] == 'Ghoul':
            return 1 


night_of_the_zealot_normal_bag = {
    '+1' : 1, '0': 0, '-1': -1, '-2': -2,
    '-3': -3,'-4': -4, 'skull': skull_value('Night of the Zealot normal'), 
    'cultist': -1, 'tablet': -2, 'Elder Sign': 1, 'auto-fail': -99}

night_of_the_zealot_normal_bag_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Sign', 'auto-fail']

#список с ключами от словаря


#для тестов
only_auto_fail_bag = {'Auto-fail': -99}
only_auto_fail_bag_keys = ['Auto-fail']
only_Elder_Sign_bag = {'Elder Sign': 1}
only_Elder_Sign_bag_keys = ['Elder Sign']

#print(night_of_the_zealot_normal_bag)

def main():
    if __name__ == '__main__':
        main()