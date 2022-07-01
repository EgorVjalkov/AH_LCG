from colorama import Fore, Back, Style
#добывляю карты оружия
#coreset weapon cards

#Rolands_38_Special_lvl0 расчеты

def Rolands_38_Special_lvl0_prefunc(fighter, enemy):
    if input('If any clues are at your location press \'y\' and \'enter\' ' ) == 'y': 
        add_skill = 3
    else: add_skill = 1
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Back.WHITE +'Roland`s .38 Special lvl0'+Back.RESET, 'class': 'Item. Weapon. Firearm', 
        'ammo': 4, 'add_skill': add_skill, 'result': result}

def Standart_postfunc(last_result):
    if last_result >= 0:
        dmg = 2
        return dmg

def Rolands_38_Special_lvl0_skillfunc():
    return {'combat': 1, 'agility': 1, 'any': 1}

Rolands_38_Special_lvl0 = {
   'prefunc': Rolands_38_Special_lvl0_prefunc, 
   'postfunc': Standart_postfunc,
   'skillfunc': Rolands_38_Special_lvl0_skillfunc}


#Gardian_weapon_cards
#Automatic_45_lvl0 расчеты

def Automatic_45_lvl0_prefunc(fighter, enemy):
    add_skill = 1
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.BLUE+'.45 Automatic lvl0'+Fore.RESET, 'class': 'Item. Weapon. Firearm', 
        'ammo': 4, 'add_skill': add_skill, 'result': result}

def Automatic_45_lvl0_skillfunc():
    return {'agility': 1}

Automatic_45_lvl0 = {
    'prefunc': Automatic_45_lvl0_prefunc, 
    'postfunc': Standart_postfunc,
    'skillfunc': Automatic_45_lvl0_skillfunc}


#Shotgun_lvl4 расчеты

def Shotgun_lvl4_prefunc(fighter, enemy):
    add_skill = 3
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.BLUE+'Shotgun lvl4'+Fore.RESET, 'class': 'Item. Weapon. Firearm', 
        'ammo': 2, 'add_skill': add_skill, 'result': result}

def Shotgun_lvl4_postfunc(last_result):
    if last_result >= 0:
        dmg = last_result + 1
        return dmg

def Shotgun_lvl4_skillfunc():
    return {'combat': 2}

Shotgun_lvl4 = {
    'prefunc': Shotgun_lvl4_prefunc, 
   'postfunc': Shotgun_lvl4_postfunc,
   'skillfunc': Shotgun_lvl4_skillfunc}


#Machete_lvl0 расчеты

def Machete_lvl0_prefunc(fighter, enemy):
    add_skill = 1
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.BLUE+'Machete lvl0'+Fore.RESET, 'class': 'Item. Weapon. Melee', 
        'add_skill': add_skill, 'result': result}

def Machete_lvl0_postfunc(last_result):
    dmg_mod = input('''If the attacked enemy is the only enemy engeged with you, 
press \'y\' and \'enter\' ''')
    if dmg_mod == 'y' and last_result >= 0:
        dmg = 2
    else: dmg = 1
    return dmg

def Machete_lvl0_skillfunc():
    return {'combat': 1}

Machete_lvl0 = {
    'prefunc': Machete_lvl0_prefunc, 
   'postfunc': Machete_lvl0_postfunc,
   'skillfunc': Machete_lvl0_skillfunc}


#Rouge_weapon_cards
#Switchblade расчеты

def Switchblade_lvl0_prefunc(fighter, enemy):
    add_skill = 0
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.GREEN+'Switchblade lvl0'+Fore.RESET, 'class': 'Item. Weapon. Melee', 
        'add_skill': add_skill, 'result': result}

def Switchblade_lvl0_postfunc(last_result):
    if last_result >= 2:
        dmg = 2
    else: dmg = 1
    return dmg

def Switchblade_lvl0_skillfunc():
    return {'agility': 1}

Switchblade_lvl0 = {
    'prefunc': Switchblade_lvl0_prefunc, 
   'postfunc': Switchblade_lvl0_postfunc,
   'skillfunc': Switchblade_lvl0_skillfunc}


#.41_Derringer_lvl0 расчеты

def Derringer_41_lvl0_prefunc(fighter, enemy):
    add_skill = 2
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.GREEN+'.41 Derringer lvl0'+Fore.RESET, 'class': 'Item. Weapon. Firearm', 
        'ammo': 3, 'add_skill': add_skill, 'result': result}

def Derringer_41_lvl0_postfunc(last_result):
    if last_result >= 2:
        dmg = 2
    else: dmg = 1
    return dmg
    
def Derringer_41_lvl0_skillfunc():
    return {'combat': 1}

Derringer_41_lvl0 = {
    'prefunc': Derringer_41_lvl0_prefunc, 
    'postfunc': Derringer_41_lvl0_postfunc,
    'skillfunc': Derringer_41_lvl0_skillfunc}


#Rouge combat events
#Backstab_lvl0 расчеты

def Backstab_lvl0_prefunc(fighter, enemy):
    fighter['combat'] = fighter['agility']
    add_skill = 0
    result = fighter['combat'] + add_skill - enemy['combat']
    return {
        'name': Fore.GREEN+'Backstab lvl0'+Fore.RESET, 'class': 'Event. Tactic', 
        'add_skill': add_skill, 'result': result}

def Backstab_lvl0_postfunc(last_result):
    return Standart_postfunc(last_result)+2

def Backstab_lvl0_skillfunc():
    return {'combat': 1, 'agility': 1}

Backstab_lvl0 = {
   'prefunc': Backstab_lvl0_prefunc, 
   'postfunc': Backstab_lvl0_postfunc,
   'skillfunc': Backstab_lvl0_skillfunc}
    
#print(Backstab_lvl0['prefunc']()['name'])


