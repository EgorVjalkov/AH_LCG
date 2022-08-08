from colorama import Fore, Back, Style


# словарь ключеевых имен и цветов
keywords2 = {
     'blue_fat': ('Guardian', 'Roland Banks', 'Nathaniel Cho', 'Daniela Reyes',), 
     'green_fat': ('Rouge', '"Skids" O`Toole', 'Winifred Habbamock', 'Monterey Jack',),
     'yellow_fat': ('Seeker', 'Daisy Walker', 'Harvey Walters', 'Norman Withers',),
     'magenta_fat': ('Mystic', 'Agnes Baker', 'Jacqueline Fine', 'Lily Chen',),
     'red_fat':('Survivor', 'Wendy Adams', 'Stella Clark', 'Bob Jenkins',),
     'red_back_with_fat': ('Ancient One', ),
     'grey_back': ('Wendy`s amulet', 'The Necronomicon. John Dee Translation'),
     'red': ('damage', 'Ghoul', 'Cultist', 'Monster', 'Auto-fail', 'combat', 'fail'),
     'dim_red': ('doom', ), 
     'blue':('horror', ), 
     'green': ('clue', 'agility', 'succeed'),
     'yellow': ('intellect', 'skull', 'cultist', 'tablet', 'Elder Thing'),
     'magenta': ('willpower', ),
     'cyan': ('Elder Sign', ),
     'fat': ('skill', 'skill test', 'token', 'cards', 'abilities', 'investigator')} # не прокрашивает слово тест. надо корректировать!

# словарь цветов
color = {
     'blue_fat': Fore.LIGHTBLUE_EX + Style.BRIGHT, 
     'green_fat': Fore.GREEN + Style.BRIGHT, 
     'yellow_fat': Fore.YELLOW + Style.BRIGHT, 
     'magenta_fat': Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
     'red_fat': Fore.LIGHTRED_EX + Style.BRIGHT, 
     'red_back_with_fat': Back.LIGHTRED_EX+Style.BRIGHT, 
     'grey_back': Back.LIGHTWHITE_EX, 
     'red': Fore.RED, 
     'dim_red': Fore.RED+Style.DIM, 
     'blue': Fore.BLUE, 
     'green': Fore.GREEN, 
     'yellow': Fore.YELLOW, 
     'magenta': Fore.MAGENTA, 
     'cyan': Fore.CYAN,
     'fat': Style.BRIGHT
     }

# принимает строку и красит каждое ее слово если находит его в словаре keywords2
def names_in_color(print_text):
     for key in keywords2:
          for i in keywords2[key]:
               if i in print_text:
                    print_text = print_text.replace(i,color[key]+i+Style.RESET_ALL)
     return print_text

# принимает строку и красит ee в соответствии с цветом text_format
def text_in_color(text, text_format):
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
colored_points_dict = {'red': 25, 'yellow': 75, 'green': 100}

# функция для окраски очков и процентов
def colored_points(points, percent):
     for key in colored_points_dict:
          if percent < colored_points_dict[key]:
               colored_percent = color[key] + (str(percent)+'%') + Style.RESET_ALL
               colored_points = color[key] + str(points) + Style.RESET_ALL
               return (colored_points, colored_percent)


#КЛЮЧЕВЫЕ ИМЕНА
keywords_names = [
     {'Class': 'Roland Banks', 'pre': Back.WHITE+Style.BRIGHT, 'post': Style.RESET_ALL},
     {'Class': 'Guardian', 'pre': Fore.BLUE, 'post': Fore.RESET}, 
     {'Class': 'Rouge', 'pre': Fore.GREEN, 'post': Fore.RESET},
     {'Class': 'Enemy', 'pre': Fore.RED, 'post': Fore.RESET},
     {'Class': 'Neutral', 'pre': Style.DIM, 'post': Style.RESET_ALL}
     ]

def colored_names(card):
     for el in keywords_names:
          if el['Class'] == card['Class']:
               colored_name = el['pre'] + card['name'] + el['post']
               card['name'] = colored_name
     return card

#main
def main():
     if __name__ == '__main__':
          string = ''
          for i in keywords2.values():
               string += ' '.join(i) + ' '
#          print(names_in_color(string))
          print(colored_scenario('The Labirinths of Lunasy standard group A'))     
          #print(colored_points(5, 99))
          
main()
