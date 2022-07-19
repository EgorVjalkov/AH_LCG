#from input_checking import input_checking as ICh
#from colored_keywords import colored_keywords as CKW 
from game_data.input_checking import input_checking as ICh # like a module
from game_data.colored_keywords import colored_keywords as CKW # like a module
from random import choice

#Сыщики
players = ('Roland Banks', 'Daisy Walker', '"Skids" O`Toole', 'Agnes Baker', 'Wendy Adams')


#Elder_Sign for Core Set investigators
def Elder_Sign(player):
    if player == 'Roland Banks': # with input check
        q =CKW('How many clues are at your location? Press a \'num\' and \'enter\' ')
        Elder_Sign = ICh(q, 'num')
    if player == '"Skids" O`Toole':
        Elder_Sign = 2
    if player == 'Daisy Walker':
        Elder_Sign = 0
    if player == 'Agnes Baker':
        q = CKW('How many horror are on Agnes Baker? Press a \'num\' and \'enter\' ')
        Elder_Sign = ICh(q, 'num') # with input check
    if player == 'Wendy Adams':
        q = CKW('Does Wendy`s amulet in play?. Press "y" or "n" and "enter" ')
        Elder_Sign = ICh(q) # with input check
        if Elder_Sign == 'y': Elder_Sign = 99
        else: Elder_Sign = 0
    return int(Elder_Sign)

#print(Elder_Sign('Roland Banks')) CORE-SET DONE!


#CORE-SET SCENARIO CHAOS TOKEN VALUES

def The_Gathering_normal_values(player):
    q = CKW('What is the number of Ghoul enemies at your location? Press a \'num\' and \'enter\' ')
    skull_value = -ICh(q, 'num') # with input check
    cultist_value = -1
    tablet_value = -2
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    return chaos_bag

def The_Midnight_Masks_values(player):
    q = CKW('What is the highest number of doom on a Cultist enemy in play? Press a \'num\' and \'enter\' ')
    skull_value = -ICh(q, 'num') # with input check
    cultist_value = -2
    tablet_value = -3
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    return chaos_bag

def The_Devouver_Below_normal_values(player):
    q = CKW('What is the number of Monster enemies in play? Press a \'num\' and \'enter\' ')
    skull_value = -ICh(q, 'num') # with input check
    cultist_value = -2
    tablet_value = -3
    Auto_fail_value = -99
    Elder_Sign_value = Elder_Sign(player)
    chaos_bag = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    q2 = CKW('Is there an Ancient One enemy in play? Press "y" or "n" and "enter" ')
    Elder_Thing = ICh(q2) # with input check
    if Elder_Thing == 'y': Elder_Thing_value = [i-5 for i in chaos_bag]
    else: Elder_Thing_value = -5
    chaos_bag.append(Elder_Thing_value)
    return chaos_bag
    
#print(The_Devouver_Below_normal_values('Agnes Baker'))

chaos_bag_values_dict = {
    'The Gathering normal': The_Gathering_normal_values, 
    'The Midnight Masks normal': The_Midnight_Masks_values, 
    'The Devourer Below normal': The_Devouver_Below_normal_values}

#ключи к сумкам

The_gathering_normal_keys = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign']

The_Devouver_Below_normal_keys = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Thing', 'Auto-fail', 'Elder Sign']

keys = {'The Gathering normal': The_gathering_normal_keys,
'The Midnight Masks normal': The_gathering_normal_keys,
'The Devourer Below normal': The_Devouver_Below_normal_keys}



# #Elder Thing
# def Elder_Thing_value(scenario, player=0):
#     token_symbol_value_for_Elder_Thing = {
#     'skull': skull_value, 'cultist': cultist_value, 'tablet': tablet_value, 
#     'Elder Sign': Elder_Sign_value}
#     if scenario == 'The Devourer Below normal': 
#         if input(CKW('Press \'y\' and \'enter\', if there is an Ancient One enemy in play ')) == 'y':
#             print('You must reveal another token')
#             The_Devouver_Below_normal_keys.remove('Elder Thing')
#             return [i-5 for i in The_Devouver_Below_normal_keys]
#         else: return -5

#print(Elder_Thing_value('The Devourer Below normal'))



#нужно разобраться со значком старцев, т.к. не понятно когда его вызывать, и куда деть вероятность, \
# как ее считать по закону вероятностей (сложение вероятностей или типа того)

#print(chaos_bag_values('The Devourer Below normal', 'Roland Banks'))