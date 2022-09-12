import json
import pyperclip


# нужно сделать запись в конец (подумай). сделай мощный пайпер клип (все данные сразу)

list_of_q_camp = ['name', 'difficulty', 'start bag', 'scenarios']
list_of_q_scenario = ['name', 'change bag']
tokens = ['skull', 'cultist', 'tablet', 'Elder Thing', 'Frost']
list_of_q_symbols = ['value', 'instant effect', 'if fail', 'reveal']


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


# write_game_data()

def probe():
    probe = pyperclip.paste()
    with open('campaign_data.json', 'a+') as data:
        data.write(json.dumps(probe, indent=3))

probe()