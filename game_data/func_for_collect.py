import json
import pyperclip


# нужно сделать запись в конец (подумай). сделай мощный пайпер клип (все данные сразу)

list_of_q_camp = ['name', 'difficulty', 'start bag', 'scenarios']
list_of_q_scenario = ['name', 'change bag']
tokens = ['skull', 'cultist', 'tablet', 'Elder Thing', 'Frost']
list_of_q_symbols = ['value', 'instant effect', 'if fail', 'reveal']

# сделай другие вопросы
def condition_with_if(token_name, description):
    try:
        condition_in_dict = {}
        condition = description[1]

        del_word_tuple = ('if', 'If', 'instead', 'you')
        condition_list = condition.split(', ')

        condition_in_dict[True] = condition_list[1]
        condition_list = condition_list[0].split()
        for word in del_word_tuple:
            question = [i for i in condition_list if i != word]

        print(question)


        # yes = condition_with_if[if_yes_index + 2:]
        # quest = condition_with_if.replace(condition_with_if[if_yes_index:], '')
        # quest_list = quest.split()
        # del quest_list[0]
        # verb = quest_list.pop(1)
        # quest_start = [f'"{token_name}":', verb]
        # quest_start.extend(quest_list)
        # quest = ' '.join(quest_start) + '?'
        # answer = quest, yes
        # return
        #
    except IndexError:
        return


condition_with_if('1', [-2, 'If there is a Monster enemy at your location, take 1 damage'])


def if_complex_value(token_name, description):
    del_word_tuple = ('if', 'If', 'instead', 'you')
    parenthesis = ('(', ')')
    try:

        value = int(description[0])

    except ValueError:
        value = description[0]
        if any(('X' in value, '(' in value)):
            if 'X' in value:
                value = description[1]
            complex_value = value.split()

            for word in del_word_tuple:
                complex_value = [i for i in complex_value if i != word]
            for symbol in parenthesis:
                complex_value = [i.replace(symbol, '') for i in complex_value if i != symbol]
                complex_value = [i for i in complex_value if i]

            if 'X' in complex_value:
                complex_value[0] = f'"{token_name}": what'
                value = ' '.join(complex_value) + '? Press "num" and "enter "'
            else:
                value = {}
                q_start = f'"{token_name}": does investigator '
                value['question'] = q_start + ' '.join(complex_value[2:]) + '? Press "y" or "n" and "enter "'
                value[True] = int(complex_value[1])
                value[False] = int(complex_value[0])
        else:
            value = 0

    return value

# print(if_complex_value('skull', ['-X', 'X is the number of Monster enemies in play']))
print(if_complex_value('skull', ['reveal']))


#print(condition_with_if('tablet', '-1 (-3 instead if you have 5 or more cards in your hand).'))
#str = 'If there is a Monster enemy at your location, take 1 damage.'
#print('If there is' in str)
#print(str.find('If'))


def write(quest_list):
    container = {}
    while True:
        for i in quest_list:
            answer = input(i + ': ')

            if i == 'value' and not answer:
                break
            if not answer:
                continue
            if answer == 'p':
                container[i] = pyperclip.paste()
                print(f'I paste {container[i]}')
            else:
                container[i] = answer

        if input(f'{container} all correct? ') == 'y':
            return container


def write_game_data():
    campaign = write(list_of_q_camp)

    for num_of_scenarios in range(int(campaign['scenarios'])):

        print(f'{num_of_scenarios+1} scenario')
        scenario = write(list_of_q_scenario)

        for num in range(len(tokens)):

            print(f'{tokens[num]}')
            symbol = write(list_of_q_symbols)
            symbol = {key: symbol[key] for key in symbol if symbol[key]}
            scenario[tokens[num]] = symbol
            # print(scenario)

        scenario = {key: scenario[key] for key in scenario if scenario[key]}
        campaign[scenario['name']] = scenario
        del scenario['name']
        # print(campaign)

    del campaign['scenarios']

    with open('campaign_data.json', 'a+') as data:
        data.write(json.dumps(campaign, indent=3))


# tokens from buffer

def token_parsing():
    while True:
        answer = input('if you copy and ready to paste press "p" : ')
        if answer == 'p':
            break
    tokens_in_str = pyperclip.paste()
    tokens_in_list = tokens_in_str.split('\n')
    tokens_in_list = [i for i in tokens_in_list if i]
    all_sorted_descriptions = []

    for i in tokens_in_list:
        description_in_dict = {}
        description = i.replace(': ', '')
        description = description.split('. ')
        value_descrip = description[0]
        negative_effect = description[1]
        # value key
        if '-X' in description:
            description_in_dict['value'] = negative_effect
            negative_effect = ''



        elif 'Reveal another token' in value_descrip:
            description_in_dict['value'] = 0

        else:
            description_in_dict['value'] = int(value_descrip)

        # if fail
        if negative_effect.find('If you fail') > 0:
            if_fail = negative_effect.relpace('If you fail, ', '')
            description_in_dict['fail'] = if_fail

        # reveal
        if 'Reveal another token' in description:
            description_in_dict['reveal'] = True
        elif negative_effect.find('reveal another token') > 0 and negative_effect.find('If') > 0:
            description_in_dict['reveal'] = negative_effect

        # instant effect
        if negative_effect:
            description_in_dict['instant effect'] = negative_effect

        all_sorted_descriptions.append(description_in_dict)

    tokens_with_description = dict(zip(tokens, all_sorted_descriptions))
    return tokens_with_description


### разберись с жетонами!!! с описанием как запарсить всякое


# write_game_data()

def probe():
    probe = pyperclip.paste()
    with open('campaign_data.json', 'a+') as data:
        data.write(json.dumps(probe, indent=3))

# probe()
# print(token_parsing())