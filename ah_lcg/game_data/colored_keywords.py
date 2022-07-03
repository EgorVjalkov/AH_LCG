from colorama import Fore, Back, Style
#import Enemies

keywords = {
     'Guardian': Fore.BLUE+'Guardian'+Fore.RESET,
     'Rouge': Fore.GREEN+'Rouge'+Fore.RESET,
     'Seeker': Fore.YELLOW+'Seeker'+Fore.RESET,
     'Mystic': Fore.MAGENTA+'Mystic'+Fore.RESET,
     'Survivor': Fore.RED+'Survivor'+Fore.RESET,
     'damage': Fore.RED+'damage'+Fore.RESET,
     'Elder Sign': Fore.CYAN+'Elder Sign'+Fore.RESET,
     'Auto-fail': Fore.RED+'Auto-fail'+Fore.RESET,
     'skull': Fore.YELLOW+'skull'+Fore.RESET,
     'cultist': Fore.YELLOW+'cultist'+Fore.RESET,
     'tablet': Fore.YELLOW+'tablet'+Fore.RESET,
     'Elder Thing': Fore.YELLOW+'Elder Thing'+Fore.RESET}

def colored_keywords(print_text):
     for key in keywords:
          if key in print_text:
              print_text = print_text.replace(key,keywords[key])
     return(print_text)

#print(colored_keywords())

keywords_names = [
     {'Class': 'Special', 'pre': Back.WHITE, 'post': Back.RESET},
     {'Class': 'Guardian', 'pre': Fore.BLUE, 'post': Fore.RESET}, 
     {'Class': 'Rouge', 'pre': Fore.GREEN, 'post': Fore.RESET},
     {'Class': 'Enemy', 'pre': Fore.RED, 'post': Fore.RESET}
     ]


def colored_names(card):
     for el in keywords_names:
          if el['Class'] == card['Class']:
               colord_name = el['pre'] + card['name'] + el['post']
               card['name'] = colord_name
     return card

#print(colored_names(Enemies.Ghoul_Minion)['name'])
