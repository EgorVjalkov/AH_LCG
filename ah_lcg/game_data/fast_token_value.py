# from input_checking import input_checking as ICh
# from colored_keywords import names_in_color as N_in_C
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
        Elder_Sign = int(ICh(q, 'num')) # with input check
    
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
        q = N_in_C(f'What is resourse cost of the top card of {player}`s deck. Press "num" and "enter" ')
        Elder_Sign = int(ICh(q, 'num')) # with input check

    if player in ('"Skids" O`Toole', 'Lily Chen'):
        Elder_Sign = 2

    if player in (
        'Nathaniel Cho','Harvey Walters', 'Winifred Habbamock', 'Jacqueline Fine', 'Stella Clark',
        'Daniela Reyes', 'Monterey Jack',  'Bob Jenkins'): 
        Elder_Sign = 1

    return Elder_Sign





# SCENARIO CHAOS TOKEN VALUES

#Core-set
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
    chaos_bag_values = [1, 0, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull_value, skull_value, cultist_value, 
    tablet_value, Auto_fail_value, Elder_Sign_value]
    return chaos_bag_values

def skull(scenario):
    value = {
        #CORE-SET
        'The Gathering standard': 'What is the number of Ghoul enemies at your location? Press a "num" and "enter" ',
        'The Midnight Masks standard': 'What is the highest number of doom on a Cultist enemy in play? Press a "num" and "enter" ',
        'The Devourer Below standard': 'What is the number of Monster enemies in play? Press a "num" and "enter" ',
        #Expansions
        'The Labyrinths of Lunasy': (-1, 'reveal')
    }
    token_value = [value[key] for key in value if key in scenario]
    if not token_value: 
        print('unknown scenario!')
        return None
    if type(token_value[0]) == str:
        if 'Press a "num" and "enter"' in token_value[0]:
            answer = -int(ICh(N_in_C(token_value[0]), 'num'))
        else: answer = (ICh(N_in_C(token_value[0])))
        return answer
    return token_value[0]

#print(skull('The Gathering standard'))


#cultist
def cultist(scenario):
    value = {
        #CORE-SET
        'The Gathering standard': -1, 'The Midnight Masks standard': -2, 'The Devourer Below standard': -2,
        #Expansions
        'The Labyrinths of Lunasy': -3
    }
    token_value = [value[key] for key in value if key in scenario]
    if not token_value: 
        print('unknown scenario!')
        return None
    return token_value[0]


#tablet
def tablet(scenario):
    value = {
        #CORE-SET
        'The Gathering standard': -2, 'The Midnight Masks standard': -2, 'The Devourer Below standard': -3,
        #Expansions
        'The Labyrinths of Lunasy': -4
    }
    token_value = [value[key] for key in value if key in scenario]
    if not token_value: 
        print('unknown scenario!')
        return None
    return token_value[0]

print(tablet('The Labyrinths of Lunasy'))


def Elder_Thing(scenario):
    value = {
        #CORE-SET
        'The Devourer Below standard': 'Is there an Ancient One enemy in play? Press "y" or "n" and "enter" ',
        #Expansions
        'The Labyrinths of Lunasy': -4
    }
    token_value = [value[key] for key in value if key in scenario]
    if not token_value: 
        print('unknown scenario!')
        return None
    if type(token_value[0]) == str:
        if 'Press a "num" and "enter"' in token_value[0]:
            print(1)
            answer = -int(ICh(N_in_C(token_value[0]), 'num'))
        else: answer = (ICh(N_in_C(token_value[0])))
        token_value = (-5, 'reveal') if answer == 'y' else -5
        return token_value
    return token_value[0]

print(Elder_Thing('The Devourer Below standard'))

    # if scenario == 'The Devourer Below standard':
    #     q2 = N_in_C()
    #     Elder_Thing = ICh(q2) # with input check
    #     value = -5
    #     if Elder_Thing == 'y':
    #         value = (-5, 'reveal')
    
    # if 'The Labyrinths of Lunasy standard' in scenario:
    #     value = -4
    # return value


#констуктор жетонов

symbol_values = {'skull': skull, 'cultist': cultist, 'tablet': tablet, 'Elder Thing': Elder_Thing, 
'Auto-fail': lambda x: -99, 'Elder Sign': Elder_Sign}

# SCENARIO CHAOS TOKEN KEYS

# Core-set
The_Gathering_standard_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Auto-fail', 'Elder Sign']
The_Devouver_Below_standard_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Elder Thing', 'Auto-fail', 'Elder Sign']

# Labirinths of Lunasy
The_Labyrinths_of_Lunasy_A_standard_keys = ['+1', '0', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', '-5',
    'skull', 'skull', 'Elder Thing', 'Elder Thing', 'Auto-fail', 'Elder Sign']
The_Labyrinths_of_Lunasy_B_standard_keys = ['+1', '0', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', '-5',
    'skull', 'skull', 'tablet', 'tablet', 'Auto-fail', 'Elder Sign']
The_Labyrinths_of_Lunasy_C_standard_keys = ['+1', '0', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', '-5',
    'skull', 'skull', 'cultist', 'cultist', 'Auto-fail', 'Elder Sign']

# для поиска по ключам
keys_dict = {
    #CORE-SET
    'The Gathering standard': The_Gathering_standard_keys,
    'The Midnight Masks standard': The_Gathering_standard_keys,
    'The Devourer Below standard': The_Devouver_Below_standard_keys,
    #The Labirinths of Lunasy
    'The Labyrinths of Lunasy standard group A': The_Labyrinths_of_Lunasy_A_standard_keys,
    'The Labyrinths of Lunasy standard group B': The_Labyrinths_of_Lunasy_B_standard_keys,       
    'The Labyrinths of Lunasy standard group C': The_Labyrinths_of_Lunasy_C_standard_keys
}

def chaos_bag_for_pulling(keys, scenario, player):
    chaos_bag_keys = keys[scenario]
    token_like_tuple = []
    el = 0
    token_value = 0
    while el < len(chaos_bag_keys):
        token_name = chaos_bag_keys[el]
        if token_name in symbol_values and token_name != 'Elder Sign':
            token_value = symbol_values[token_name](scenario)
        elif token_name == 'Elder Sign': 
            token_value = symbol_values[token_name](player)
        else:
            token_value = int(token_name)
        count_of_similar = chaos_bag_keys.count(token_name)
        for i in range(count_of_similar):
            token_like_tuple.append((token_name, token_value))
        el += count_of_similar
    return token_like_tuple

def chaos_bag_for_probability(chaos_bag):
    dict_of_tokens = {}
    reveal_tokens = list(filter(lambda x: type(x[1]) == tuple, chaos_bag))
    chaos_bag_for_dict = list(filter(lambda x: type(x[1]) != tuple, chaos_bag))
    dict_of_tokens['bag'] = [token[1] for token in chaos_bag_for_dict]
    divider = len(chaos_bag)
    dict_of_tokens['bag divider'] = divider
    num = 1
    for i in reveal_tokens:
        token_name = i[0] + str(num)
        token_value = i[1][0]
        dict_of_tokens[f'{token_name}+'] = [token_value+value for value in dict_of_tokens['bag']]
        num += 1
        # if len(reveal_tokens) == 2 and num == 2:
        #     token_name = list(dict_of_tokens.keys())[2] + token_name
        #     token_value =  + token_value
        #     dict_of_tokens[f'{token_name}+'] = [token_value+value for value in dict_of_tokens['bag']]
        #     divider_for_reveal_token *= divider
        #     dict_of_tokens[f'{token_name}+ divider'] = divider_for_reveal_token
    return(dict_of_tokens)


#main_func
def main():
    if __name__ == '__main__':
#        print(The_Devouver_Below_standard_values('Lily Chen'))
#        print(Elder_Sign('Nathaniel Cho'))
        bag = chaos_bag_for_pulling(keys_dict, 'The Labyrinths of Lunasy standard group C', 'Roland Banks')
        print(bag)
        print(chaos_bag_for_probability(bag) )

main()
