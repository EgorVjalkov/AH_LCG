from colorama import Fore, Back, Style
import Enemies

keywords = {
     'Guardian': Fore.BLUE+'Guardian'+Fore.RESET,
     'Rouge': Fore.GREEN+'Rouge'+Fore.RESET,
     'Seeker': Fore.YELLOW+Style.DIM+'Seeker'+Style.RESET_ALL,
     'Mystic': Fore.MAGENTA+'Mystic'+Fore.RESET,
     'Survivor': Fore.RED+'Survivor'+Fore.RESET,
     'damage': Fore.RED+Style.DIM+'damage'+Style.RESET_ALL,
     'horror': Fore.BLUE+Style.DIM+'horror'+Style.RESET_ALL,
     'Elder Sign': Fore.CYAN+'Elder Sign'+Fore.RESET,
     'Auto-fail': Fore.RED+'Auto-fail'+Fore.RESET,
     'skull': Fore.YELLOW+'skull'+Fore.RESET,
     'cultist': Fore.YELLOW+'cultist'+Fore.RESET,
     'tablet': Fore.YELLOW+'tablet'+Fore.RESET,
     'Elder Thing': Fore.YELLOW+'Elder Thing'+Fore.RESET,
     'willpower': Fore.MAGENTA+'willpower'+Fore.RESET,
     'combat': Fore.RED+'combat'+Fore.RESET,
     'intellect': Fore.YELLOW+Style.DIM+'Seeker'+Style.RESET_ALL,
     'agility': Fore.GREEN+'agility'+Fore.RESET,
     }

def colored_keywords(print_text):
     for key in keywords:
          if key in print_text:
              print_text = print_text.replace(key,keywords[key])
     return(print_text)

print(colored_keywords('intellect'))

keywords_names = [
     {'Class': 'Special', 'pre': Back.WHITE, 'post': Back.RESET},
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

print(colored_names(Enemies.Ghoul_Minion)['name'])
