from colorama import Fore, Back, Style
import cards

keywords = {
     'Guardian': Fore.BLUE+'Guardian'+Fore.RESET,
     'Rouge': Fore.GREEN+'Rouge'+Fore.RESET,
     'Seeker': Fore.YELLOW+'Seeker'+Fore.RESET,
     'Mystic': Fore.MAGENTA+'Mystic'+Fore.RESET,
     'Survivor': Fore.RED+'Survivor'+Fore.RESET,
     'Guardian': Fore.BLUE+'Guardian'+Fore.RESET}

def colored_keywords(print_text):
     for key in keywords:
          if key in print_text:
              print_text = print_text.replace(key,keywords[key])
     return(print_text)



keywords_names = [{'Class': 'Guardian', 'pre': Fore.BLUE, 'post': Fore.RESET}, 2]
#print(keywords_names[0])

TypeError: list indices must be integers or slices, not dict

def colored_names(card):
     for el in keywords_names:
          print(keywords_names[el])
          if keywords_names[i]['Class'] == card['Class']:
               colord_name = keywords_names[i]['pre'] + card['name'] + keywords_names[i]['post']
               card['name'] = colord_name
     print(card['name'])

Automatic = {
        'name': '.45 Automatic lvl0', 'Class': 'Guardian', 'traits': 'Item. Weapon. Firearm', 
        'ammo': 4, 'add_skill': 1, 'result': 1}

colored_names(Automatic)

#colored_keywords('SEFSFSEFSFSE, Rouge SEFSEFSEF. combat +SEFSEFS. Guardian...Automatic', Automatic)