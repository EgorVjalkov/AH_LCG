#from game_data.Roland_Banks import Roland_Banks
#from game_data.scenario_token_value import *
from probability_for_action import short_probability, pull_a_token
from game_data.cards import *
from colorama import Fore, Back, Style

#раскрась имена сыщиков и монстров
#chaos_bag = only_auto_fail_bag
#chaos_bag_keys = only_auto_fail_bag_keys

Roland = {'name': 'Roland_Banks', 'combat': 1, 'agility': 2}
Ghoul = {'name': 'Ghoul', 'combat': 2, 'health': 3, 'agility': 2, 'damage':1, 'horror':1, 'keywords': 'retaliate'}
#add_skill = 1

def fight_action(fighter, enemy, asset_or_event={}):
     investigator_name = fighter['name']
     enemy_name = enemy['name']
     if not asset_or_event: 
          result = fighter['combat'] - enemy['combat']
          asset_or_event = {'name': 'unarmed', 'class': 'Weapon. Melee','add_skill': 0, 'result': result}
     weapon_name = asset_or_event['name']
     before_token_result = asset_or_event['prefunc'](fighter,enemy)
     print(f'You have a {before_token_result} points.')
     short_probability(before_token_result, chaos_bag, chaos_bag_keys)
#Add_a_card     
     final_result = pull_a_token(chaos_bag, chaos_bag_keys, before_token_result, enemy['combat'])
     if final_result >= 0:
          dmg = asset_or_event['postfunc'](final_result)
          print(f'Success! {investigator_name} deals {enemy_name} {dmg} point(s) of damage by {weapon_name}')
          if enemy['health'] - dmg <= 0:
               print('Enemy down!')
     else:
          print('Failure!')
          if 'retaliate' in enemy['keywords']:
               retalite_damage = enemy['damage']
               retalite_horror = enemy['horror']
               print(f'{enemy_name} deals {investigator_name} {retalite_damage} damage and {retalite_horror} horror')

keywords = {'Guardian': Fore.BLUE+'Guardian'+Fore.RESET}

def colored_keywords(print_text):
     list_of_coords = []
     for i in print_text:
          if not i.isalpha():
               if i != ' ':
                    index = print_text.index(i)
                    coords = dict.fromkeys([i], index)
                    list_of_coords.append(coords)
                    print_text = print_text.replace(i, ' ', 1)
     print(list_of_coords, print_text)
     for word in print_text:# остановнка здесь. нужно доделать, поставить знаки на их индексы и раскрасить слова конечно!!!
          if word in keywords:
               i = words.index(word)
               print(i)
               words.remove(word)
               colored_word = keywords[word]
               words.insert(i, colored_word)
     colored_text = ' '.join(words)
     # print(colored_text)
     
colored_keywords('SEFSFSEFSFSE, SEFSEFSEF. +SEFSEFS. Guardian...')
#fight_action(Roland, Ghoul, Rolands_38_Special_lvl0)