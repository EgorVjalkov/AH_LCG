from colorama import Fore, Back, Style
#import Enemies

keywords2 = {
     'blue_back': ('Guardian', 'Roland Banks'), 
     'green_back': ('Rouge', '"Skids" O`Toole'),
     'yellow_back': ('Seeker', 'Daisy Walker'),
     'magenta_back': ('Mystic', 'Agnes Baker'),
     'red_back':('Survivor', 'Wendy Adams'),
     'red_back_with_fat': ('Ancient One', ),
     'grey_back': ('Wendy`s Amulet', ),
     'red': ('damage', 'Ghoul', 'Cultist', 'Monster', 'Auto-fail', 'combat', 'fail'),
     'dim_red': ('doom', ), 
     'blue':('horror', ), 
     'green': ('clue', 'agility', 'succeed'),
     'yellow': ('intellect', 'skull', 'cultist', 'tablet', 'Elder Thing'),
     'magenta': ('willpower', ),
     'cyan': ('Elder Sign', ),
     'fat': ('skill', 'skill_test', 'token')} # не прокрашивает слово тест. надо корректировать!

color = {
     'blue_back': Back.LIGHTBLUE_EX, 'green_back': Back.GREEN, 'yellow_back': Back.YELLOW, 
     'magenta_back': Back.LIGHTMAGENTA_EX, 'red_back': Back.LIGHTRED_EX, 
     'red_back_with_fat': Back.LIGHTRED_EX+Style.BRIGHT, 'grey_back': Back.LIGHTWHITE_EX, 'red': Fore.RED, 'dim_red': Fore.RED+Style.DIM, 
     'blue': Fore.BLUE, 'green': Fore.GREEN, 'yellow': Fore.YELLOW, 'magenta': Fore.MAGENTA, 'cyan': Fore.CYAN,
     'fat': Style.BRIGHT
     }

def names_in_color(print_text):
     for key in keywords2:
          for i in keywords2[key]:
               if i in print_text:
                    print_text = print_text.replace(i,color[key]+i+Style.RESET_ALL)
     return print_text

# проверка словаря
string = ''
for i in keywords2.values():
    string += ' '.join(i) + ' '
#print(names_in_color(string))


#Color for scenario names
scenario_color = {
     'easy': Fore.LIGHTBLACK_EX,
     'standard': Fore.YELLOW,
     'hard': Fore.RED,
     'expert': Fore.RED+Style.BRIGHT
}

def colored_scenario(name):
     for key in scenario_color:
          if key in name:
               colored_name = scenario_color[key]+name+Style.RESET_ALL
               return colored_name

#print(colored_scenario('sejfslejhf lsjefeasy'))

colored_points_dict = {'red': 25, 'yellow': 75, 'green': 100}

def colored_points(points, percent):
     for key in colored_points_dict:
          if percent < colored_points_dict[key]:
               colored_percent = color[key] + (str(percent)+'%') + Style.RESET_ALL
               colored_points = color[key] + str(points) + Style.RESET_ALL
               return (colored_points, colored_percent)

#print(colored_points(5, 99))




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

# Rolands_38_Special_lvl0 = {
#     'name': 'Roland`s .38 Special lvl0', 'Class': 'Roland Banks', 
#     'type': 'asset', 'lvl': 0, 'cost': 3, 
#     'traits': 'Item. Weapon. Firearm', 'uses': 4, 
#     'using': '''Spend 1 ammo: Fight. You get +1 combat for this attack 
#     (if there are 1 or more clues on your location, you get +3 combat, instead). 
#     This attack deals +1 damage.'''}

#print(colored_names(Rolands_38_Special_lvl0)['name'])

# def main():
#      if __name__ == '__main__':
#           main()
