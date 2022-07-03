from game_data.colored_keywords import colored_keywords as CKW, colored_names as CN # цветные имена
from probability_for_action import short_probability, pull_a_token # импорт функций
from game_data.cards import Rolands_38_Special_lvl0 # импорт карт
from game_data.scenario_token_value import only_auto_fail_bag, only_auto_fail_bag_keys # сумки
from game_data.investigators import Roland_Banks #импорт сыщиков
from game_data.Enemies import Ghoul_Minion #импорт врагов
# нет быстрых карт и карт навыков. в работе

chaos_bag = only_auto_fail_bag
chaos_bag_keys = only_auto_fail_bag_keys

#add_skill = 1

def fight_action(fighter, enemy, asset_or_event={}):
     investigator_name = fighter['name']
     enemy_name = enemy['name']
     #print(enemy['fight'])
     if not asset_or_event: 
          result = fighter['combat'] - enemy['combat']
          asset_or_event = {'name': 'unarmed', 'class': 'Weapon. Melee','add_skill': 0, 'result': result}
     weapon_name = asset_or_event['name']
     before_token_result = asset_or_event['prefunc'](fighter,enemy)['result']
     print(f'You have a {before_token_result} points.')
     short_probability(before_token_result, chaos_bag, chaos_bag_keys)
#Add_a_card     
     final_result = pull_a_token(chaos_bag, chaos_bag_keys, before_token_result, enemy['fight'])
     if final_result >= 0:
          dmg = asset_or_event['postfunc'](final_result)
          print(CKW(f'Success! {investigator_name} deals {enemy_name} {dmg} point(s) of damage by {weapon_name}'))
          if enemy['health'] - dmg <= 0:
               print(CKW('Enemy down!'))
     else:
          print(CKW('Failure!'))
          if 'keywords' in enemy:
               retalite_damage = enemy['damage']
               retalite_horror = enemy['horror']
               print(CKW(f'{enemy_name} deals {investigator_name} {retalite_damage} damage and {retalite_horror} horror'))

#print(CN(Ghoul_Minion)['name'])
fight_action(CN(Roland_Banks), CN(Ghoul_Minion), CN(Rolands_38_Special_lvl0))