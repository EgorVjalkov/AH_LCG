from colorama import Fore

#current_player = {'name': 'Roland_Banks', 'actions': 3, 'status': 'at_combat'}

#хз как организовать, думать надо!

#def Roland_Banks_special():
#    if current_player['name'] == 'Roland_Banks' and current_player['status'] == 'at combat' and 

def Roland_Banks_Elder_Sign():
    Elder_Sign = int(input('does any clue at your location? Press a \'num\' and \'enter\' '))
    return Elder_Sign


Roland_Banks = {
    'name': Fore.BLUE+'Roland Banks', 'class': Fore.BLUE+'Guardian', 
    'willpower': 3, 'intellect': 3, 'combat': 4, 'agility': 2,
    'special': Roland_Banks_special, 'Elder_Sign_value': Roland_Banks_Elder_Sign
}


#print(Roland_Banks['name'])
#special = 'After you defeat an enemy: discover 1 clue at your location (Limit once per round)'
#elder_sign_effect = '+1 for each clue on your location'