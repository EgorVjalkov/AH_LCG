from colorama import Fore, Back, Style
#import Enemies


keywords = {
     'Guardian': Back.BLUE+Style.BRIGHT+'Guardian'+Style.RESET_ALL,
     'Rouge': Back.GREEN+Style.BRIGHT+'Rouge'+Style.RESET_ALL,
     'Seeker': Back.YELLOW+Style.BRIGHT+'Seeker'+Style.RESET_ALL,
     'Mystic': Back.MAGENTA+Style.BRIGHT+'Mystic'+Style.RESET_ALL,
     'Survivor': Back.RED+Style.BRIGHT+'Survivor'+Style.RESET_ALL,
     'damage': Fore.RED+Style.BRIGHT+'damage'+Style.RESET_ALL,
     'doom': Fore.RED+Style.DIM+'doom'+Style.RESET_ALL,
     'horror': Fore.BLUE+Style.BRIGHT+'horror'+Style.RESET_ALL,
     'clue': Fore.GREEN+Style.BRIGHT+'clue'+Style.RESET_ALL,
     'Elder Sign': Fore.CYAN+'Elder Sign'+Fore.RESET,
     'Auto-fail': Fore.RED+'Auto-fail'+Fore.RESET,
     'skull': Fore.YELLOW+'skull'+Fore.RESET,
     'cultist': Fore.YELLOW+'cultist'+Fore.RESET,
     'tablet': Fore.YELLOW+'tablet'+Fore.RESET,
     'Elder Thing': Fore.YELLOW+'Elder Thing'+Fore.RESET,
     'willpower': Fore.MAGENTA+'willpower'+Fore.RESET,
     'combat': Fore.RED+'combat'+Fore.RESET,
     'intellect': Fore.YELLOW+Style.DIM+'intellect'+Style.RESET_ALL,
     'agility': Fore.GREEN+'agility'+Fore.RESET,
     'Ghoul': Fore.RED+'Ghoul'+Fore.RESET,
     'Cultist': Fore.RED+'Cultist'+Fore.RESET,
     'Monster': Fore.RED+'Monster'+Fore.RESET,
     'Ancient One': Back.RED+Style.BRIGHT+'Ancient One'+Style.RESET_ALL}

def colored_keywords(print_text):
     for key in keywords:
          if key in print_text:
               print_text = print_text.replace(key,keywords[key])
     return(print_text)


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

print(colored_keywords('clues'))
print(colored_keywords(' '.join(keywords.keys())))