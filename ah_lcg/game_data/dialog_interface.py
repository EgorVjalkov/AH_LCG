if __name__ == '__main__':
    from input_checking import input_checking as ICh
    from colored_keywords import names_in_color as N_in_C, text_in_color as T_in_C
else:    
    from game_data.input_checking import input_checking as ICh # like a module
    from game_data.colored_keywords import names_in_color as N_in_C, text_in_color as T_in_C # like a module


#функция меню
def menu(menu_dict, player):
    menu = {}
    for num, el in enumerate(list(menu_dict.keys())[1:]):
        print(N_in_C(f'press "{num+1}" and "enter" - {el}')) # печать пунктов меню
        menu[str(num+1)] = el
    q = menu_dict['description'](player)
    limit_of_answer = tuple(str(i) for i in range(1, len(menu.keys())+1))
    answer = ICh(q, limit_of_answer) # проверка ввода 
    menu_answer_in_menu_dict = ''.join([menu[answer]])
    print('') # отступ
    print(N_in_C(f'{player} try to {menu_answer_in_menu_dict}'))
    return menu_dict[menu[answer]]

#меню с применением карт
card_using_menu_dict = {
    'description': lambda player: N_in_C(player) + T_in_C(' reads a discription of a card, is there one of expressions in? ', 'fat'),
    'succeed a skill test by 1 or more': (1, 'succeed by or more'),
    'succeed a skill test by 2 or more': (2, 'succeed by or more'),
    'succeed a skill test by 3 or more': (3,'succeed by or more'),
    'succeed a skill test by 4 or more': (4, 'succeed by or more'),
    'fail a skill test by 2 or less': (-2, 'fail by or less'),
    'fail a skill test by 2 or more': (-2, 'fail by or more'),
    'no expressions': 'exit'
}

dict_of_cards_or_abilities = {}

#основное меню
general_menu = {
    'description': lambda player: T_in_C('What does ', 'fat') + N_in_C(player) + T_in_C(' try to do? ', 'fat'),
    'pull a token': 'exit', 
    'add skill point(s) and pull a token': lambda player: int(ICh('How many points does ' + N_in_C(player) + ' try to add? ', 'num')),
    'recalculate a probability (if use some cards or abilities)': lambda player: menu(card_using_menu_dict, player),
    #'view a list of cards and abilities (whitch would be able to use for a skill test)': None
}
    
#main_func
def main():
    if __name__ == '__main__':
        answer = menu(general_menu, 'Wendy Adams')
        answer2 = answer('Wendy Adams')
        if type(answer2) == int:
            print(answer2)

main()


# Lucky!(если провал +2), Sure Gamble (Switch + on -), Daring Maneuver (если успех еще +2)
# Ritual Candles (+1 symbol), Crystal Pendulum (enter a number), Dark Prophecy (5 tokens), 
# Defiance (nignore a token), Grotesque Statue (2 tokens instead 1), Grannie Orne (+1 or -1),
# 21 or Bust (игра в очко. интересная механика), Money Talks (че-то там с ресурсами), 
# Snipe(symbols is 0), Nkosi Mabati: Enigmatic Warlock (sigil), Divination (succeed by 0), 
#"Hit me!" (+1 token), Precious Memento: From a Former Life (+2 -2)
    


