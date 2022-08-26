
print('greet')

GAME = True
INPUT = True
CALCULATE = {'result': True, 'bag': True}
PULL_TOKEN = True

while GAME:

    if INPUT:
        print('Start a new skill test')
        INPUT = False

    if CALCULATE['result'] or CALCULATE['bag']:

        if CALCULATE['result']:
            result = 'calc result'
            print(result)
            CALCULATE['result'] = False

        if CALCULATE['bag']:
            bag = 'calc bag'
            print(bag)
            CALCULATE['bag'] = False

        print('tabla')

    x = input('change result? ')
    if x == 'y':
        print('you change result')
        CALCULATE['result'] = True
        PULL_TOKEN = False

    y = input('change bag? ')
    if y == 'y':
        print('you change bag')
        CALCULATE['bag'] = True
        PULL_TOKEN = False

    if not x and not y:
        print('You pull a token. Cycle ended')
        INPUT = True
        CALCULATE = {'result': True, 'bag': True}
