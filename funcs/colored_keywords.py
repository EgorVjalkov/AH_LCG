from colorama import Fore, Back, Style


# МЕЛОЧИ НУЖНО ПОПРАВИТЬ: SKILL И SKILL TEST. FAIL И AUTO-FAIL!!!!


# словарь ключеевых имен и цветов


keywords2 = {
     'blue_fat': ('Guardian', 'Roland Banks', 'Nathaniel Cho', 'Daniela Reyes',), 
     'green_fat': ('Rouge', '"Skids" O`Toole', 'Winifred Habbamock', 'Monterey Jack',),
     'yellow_fat': ('Seeker', 'Daisy Walker', 'Harvey Walters', 'Norman Withers',),
     'magenta_fat': ('Mystic', 'Agnes Baker', 'Jacqueline Fine', 'Lily Chen',),
     'red_fat': ('Survivor', 'Wendy Adams', 'Stella Clark', 'Bob Jenkins',),
     'red_back': ('Ancient One', ),
     'grey_back': ('Wendy`s amulet', 'The Necronomicon, John Dee Translation'),
     'red': ('damage', 'Ghoul', 'Cultist', 'Monster', '"Auto-fail"', 'combat', 'fail'),
     'dim_red': ('doom', ), 
     'blue': ('horror', '"Frost"'),
     'green': ('clue', 'agility', 'succeed'),
     'yellow': ('intellect', '"skull"', '"cultist"', '"tablet"', '"Elder Thing"'),
     'magenta': ('willpower', ),
     'cyan': ('"Elder Sign"', ),
     'fat': ('skill', 'skill test', 'token', 'cards', 'abilities', 'investigator')} # не прокрашивает слово тест. надо корректировать!

# словарь цветов
color = {
     'blue_fat': Fore.LIGHTBLUE_EX + Style.BRIGHT, 
     'green_fat': Fore.GREEN + Style.BRIGHT, 
     'yellow_fat': Fore.YELLOW + Style.BRIGHT, 
     'magenta_fat': Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
     'red_fat': Fore.LIGHTRED_EX + Style.BRIGHT,
     'grey_back': Back.WHITE + Fore.BLACK,
     'red': Fore.RED, 
     'dim_red': Fore.RED+Style.DIM, 
     'blue': Fore.BLUE, 
     'green': Fore.GREEN, 
     'yellow': Fore.YELLOW, 
     'magenta': Fore.MAGENTA, 
     'cyan': Fore.CYAN,
     'fat': Style.BRIGHT,
     'red_back': Back.RED + Fore.BLACK,
     'yellow_back': Back.YELLOW + Fore.BLACK,
     'green_back': Back.GREEN + Fore.BLACK
     }


# принимает строку и красит каждое ее слово если находит его в словаре keywords2
def names_in_color(print_text):
    for key in keywords2:
        for i in keywords2[key]:
            if i in print_text:
                print_text = print_text.replace(i, color[key]+i+Style.RESET_ALL)
    return print_text


# принимает строку и красит ee в соответствии с цветом text_format
def text_in_color(text, text_format='fat'):
     color_func = color[text_format]
     colored_text = color_func + text + Style.RESET_ALL
     return colored_text


#Color for scenario names
scenario_color = {
     'easy': Fore.LIGHTBLACK_EX,
     'standard': Fore.YELLOW,
     'hard': Fore.RED,
     'expert': Fore.RED+Style.BRIGHT
}


# принимает имя сценария и красит его по словарю scenario_color
def colored_scenario(name):
    for key in scenario_color:
        if key in name:
            colored_name = scenario_color[key]+name+Style.RESET_ALL
            return colored_name
    else:
        return name


# словарь для окраски очков и процентов
colored_points_dict = {'red': 30, 'yellow': 70, 'green': 100}
result_points_dict = {'red_back': 30, 'yellow_back': 70, 'green_back': 100}


# функция для окраски очков и процентов


def colored_points(points, percent):
    color_key = tuple(key for key in result_points_dict if result_points_dict[key] > percent)[0]
    colored_percent = color[color_key] + (str(percent)+'%') + Style.RESET_ALL
    colored_points = color[color_key] + str(points) + Style.RESET_ALL
    return colored_points, colored_percent


#main
def main():
    if __name__ == '__main__':
        string = ''
        for i in keywords2.values():
            string += ' '.join(i) + ' '
#           print(names_in_color(string))
        a = colored_points(4, 15)
        print(len(a[0]))
        print(a)
        print(text_in_color('|a|', 'fat'))
        print(names_in_color('"Auto-fail", "Auto-fail'))


main()
