#from input_checking import input_checking as ICh
#from colored_keywords import names_in_color as N_in_C
from game_data.input_checking import input_checking as ICh
from game_data.colored_keywords import names_in_color as N_in_C


dialog_interface_dict = {
        'to succeed a skill test by 2 or more': 2,
        'to succeed a skill test by 3 or more': 3,
        'to succeed a skill test by 4 or more': 4,
        'to succeed a skill test or fail a skill test by 2 or less': (-1, -2),
        }

# Lucky!(если провал +2), Sure Gamble (Switch + on -), Daring Maneuver (если успех еще +2)
# Ritual Candles (+1 symbol), Crystal Pendulum (enter a number), Dark Prophecy (5 tokens), 
# Defiance (nignore a token), Grotesque Statue (2 tokens instead 1), Grannie Orne (+1 or -1),
# 21 or Bust (игра в очко. интересная механика), Money Talks (че-то там с ресурсами), 
# Snipe(symbols is 0), Nkosi Mabati: Enigmatic Warlock (sigil), Divination (succeed by 0), 
#"Hit me!" (+1 token), Precious Memento: From a Former Life (+2 -2)
def dialog_interface():
    menu = {}
    for num, el in enumerate(dialog_interface_dict.keys()):
        print(N_in_C(f'press "{num+1}" and "enter" - {el}'))
        menu[str(num+1)] = el
    q = ': ' # input check
    answer = ICh(q, ('1','2','3','4')) # input check
    return dialog_interface_dict[menu[answer]]

general_menu = {
    '1': 'to add skill point(s) and pull a token', 
    '2': 'to pull a token', 
    '3': 'to succeed or fail a skill test by "?" and recalculate a probability'}
    
    
    
    
    
    # for num, el in enumerate(dialog_interface_dict.keys()):
    #     menu_point = num, el
    #     menu.append(num,el)
    #     print(N_in_C(f'press "{num+1}" and "enter" - {el}'))



    


#print(dialog_interface(5, 'Egorok'))