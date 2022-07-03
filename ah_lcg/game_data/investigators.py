investigators_list = [
    'Roland Banks']


#Roland Banks

def Roland_Banks_Elder_Sign():
    Elder_Sign = int(input('does any clue at your location? Press a \'num\' and \'enter\' '))
    return Elder_Sign

def Roland_Banks_special():
    pass #пока не придумал


Roland_Banks = {
    'name': 'Roland Banks', 'Class': 'Guardian', 
    'willpower': 3, 'intellect': 3, 'combat': 4, 'agility': 2,
    'Special': Roland_Banks_special, 'Elder Sign': Roland_Banks_Elder_Sign
}


#special = 'After you defeat an enemy: discover 1 clue at your location (Limit once per round)'
#elder_sign_effect = '+1 for each clue on your location'