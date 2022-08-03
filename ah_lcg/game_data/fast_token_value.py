if __name__ == '__main__':
    from input_checking import input_checking as ICh
    from colored_keywords import names_in_color as N_in_C
else:    
    from game_data.input_checking import input_checking as ICh # like a module
    from game_data.colored_keywords import names_in_color as N_in_C # like a module

#Сыщики
players = (
    'Roland Banks', 'Daisy Walker', '"Skids" O`Toole', 'Agnes Baker', 'Wendy Adams', #CORE-SET
    'Nathaniel Cho','Harvey Walters', 'Winifred Habbamock', 'Jacqueline Fine', 'Stella Clark', # investigator expansions
    'Daniela Reyes', 'Norman Withers', 'Monterey Jack', 'Lily Chen', 'Bob Jenkins', # Edge of The Earth
)


#Elder_Sign for Core Set investigators
def Elder_Sign(player):
    if player == 'Roland Banks': 
        q =N_in_C('How many clues are at your location? Press a \'num\' and \'enter\' ')
        Elder_Sign = int(ICh(q, 'num'))
    
    if player == 'Daisy Walker':
        q = N_in_C('Does The Necronomicon. John Dee Translation in play?. Press "y" or "n" and "enter" ')
        Elder_Sign = ICh(q) # with input check
        if Elder_Sign == 'y': Elder_Sign = -99
        else: Elder_Sign = 0

    if player == 'Agnes Baker':
        q = N_in_C('How many horror are on Agnes Baker? Press a \'num\' and \'enter\' ')
        Elder_Sign = int(ICh(q, 'num')) # with input check

    if player == 'Wendy Adams':
        q = N_in_C('Does Wendy`s amulet in play?. Press "y" or "n" and "enter" ') # !!!! не окрвсился
        Elder_Sign = ICh(q) # with input check
        if Elder_Sign == 'y': Elder_Sign = 99
        else: Elder_Sign = 0

    if player == 'Norman Withers':
        q = N_in_C(f'What resourse cost of the top card of {player}`s deck. Press "num" and "enter" ')
        Elder_Sign = int(ICh(q, 'num')) # with input check

    if player in ('"Skids" O`Toole', 'Lily Chen'):
        Elder_Sign = 2

    if player in (
        'Nathaniel Cho','Harvey Walters', 'Winifred Habbamock', 'Jacqueline Fine', 'Stella Clark',
        'Daniela Reyes', 'Monterey Jack',  'Bob Jenkins'): 
        Elder_Sign = 1

    return Elder_Sign


#CORE-SET DONE!


#CORE-SET SCENARIO CHAOS TOKEN VALUES


#ключи к сумкам

The_gathering_standard_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign']

The_Devouver_Below_standard_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign', 'Elder Thing']

keys = {'The Gathering standard': The_gathering_standard_keys,
'The Midnight Masks standard': The_gathering_standard_keys,
'The Devourer Below standard': The_Devouver_Below_standard_keys}


def The_Gathering_standard_values(player):
    q = N_in_C('What is the number of Ghoul enemies at your location? Press a \'num\' and \'enter\' ')
    skull_value = -int(ICh(q, 'num')) # with input check
    cultist_value = -1
    tablet_value = -2
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag_values = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    return chaos_bag_values

def The_Midnight_Masks_standard_values(player):
    q = N_in_C('What is the highest number of doom on a Cultist enemy in play? Press a \'num\' and \'enter\' ')
    skull_value = -int(ICh(q, 'num')) # with input check
    cultist_value = -2
    tablet_value = -3
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag_values = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    return chaos_bag_values

def The_Devouver_Below_standard_values(player):
    q = N_in_C('What is the number of Monster enemies in play? Press a \'num\' and \'enter\' ')
    skull_value = -int(ICh(q, 'num')) # with input check
    cultist_value = -2
    tablet_value = -3
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag_values = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    q2 = N_in_C('Is there an Ancient One enemy in play? Press "y" or "n" and "enter" ')
    Elder_Thing = ICh(q2) # with input check
    if Elder_Thing == 'y': Elder_Thing_value = [i-5 for i in chaos_bag_values]
    else: Elder_Thing_value = -5
    chaos_bag_values.append(Elder_Thing_value)
    return chaos_bag_values


#значение сумок

chaos_bag_values_dict = {
    'The Gathering standard': The_Gathering_standard_values, 
    'The Midnight Masks standard': The_Midnight_Masks_standard_values, 
    'The Devourer Below standard': The_Devouver_Below_standard_values}

#main_func
def main():
    if __name__ == '__main__':
#        print(The_Devouver_Below_standard_values('Stella Clark'))
        print(Elder_Sign('Nathaniel Cho')) 

main()
