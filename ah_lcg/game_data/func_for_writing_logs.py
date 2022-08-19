import csv
from datetime import datetime


today = datetime.today().strftime('%d.%m.%Y')
now = datetime.now().strftime('%H:%M')


def write_start_game(scenario, investigators):
    if len(investigators) > 1:
        other_investigators_in_str = ', '.join(investigators[1:])
        type_game = f'Coop game. Other investigator(s) is(are) {other_investigators_in_str}'
    else:
        type_game = 'Solo game'
    log_entry = [today, now, 'start new game', scenario, investigators[0], type_game]
    with open('/home/egorok/AH_LCG/ah_lcg/logs/logs.csv', 'w') as logs:
        writer = csv.writer(logs)
        writer.writerow(log_entry)


def write_checking(player, skill, skill_test, success):
    result = skill - skill_test
    success = success[0] + '%'
    log_entry = [today, now, 'checking', player, skill, skill_test, result, success]

    with open('/home/egorok/AH_LCG/ah_lcg/logs/logs.csv', 'a') as logs:
        writer = csv.writer(logs)
        writer.writerow(log_entry)


def write_reveal(player, tokens, value, result, total):
    log_entry = [today, now, 'revealing', player, tokens, value, result, total]

    with open('/home/egorok/AH_LCG/ah_lcg/logs/logs.csv', 'a') as logs:
        writer = csv.writer(logs)
        writer.writerow(log_entry)
        writer.writerow([])


def write_adding(player, points):
    log_entry = [today, now, 'adding', player, points]

    with open('/home/egorok/AH_LCG/ah_lcg/logs/logs.csv', 'a') as logs:
        writer = csv.writer(logs)
        writer.writerow(log_entry)


write_a_log = {
    'start game': write_start_game,
    'checking': write_checking,
    'adding': write_adding,
    'revealing': write_reveal
}
