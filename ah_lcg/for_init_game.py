from AH_LCG.ah_lcg.game_data.investigators import investigators_list


def choose_an_investigator():
    print('Choose your investigator: ' + ', '.join(investigators_list))
    investigator1 = input('An investigator1: ')
    while not investigator1 in investigators_list:
        print('incorrect name!')
        investigator1 = input('Choose investigator1 again: ')
    print('done!')
    investigator2 = input('An investigator2: ')
    if not investigator2:
        return investigator1
    while not investigator2 in investigators_list:
        print('incorrect name!')
        investigator2 = input('Choose investigator2 again: ')
    print('done!')
    return investigator1, investigator2

#choose_an_investigator()

def create_chaos_bag():        
    tokens = ['+1', '0', '-1', '-2', '-3', '-4', '-5', '-6', 
    'skull', 'cultist', 'tablet', 'Elder Thing', 'Auto-fail', 'Elder Sign']
    new_bag = []
    for i in tokens:
        n = 1
        a = int(input(f'Enter count of {i} token:\n'))
        if a >= n:
            while n <= a: 
                new_bag.append(i)
                n += 1
    return new_bag

#print(id(create_chaos_bag()))