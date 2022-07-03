# прочитай про мэйн, сделай так, чтобы не собирать все сумки подряд
#сделай хрень с жетонами, типа там удар на таблетку ну ты понял. 

#значения жетонов
# night_of_the_zealot_normal_bag = {
#     '+1' : 1, '0': 0, '-1': -1, '-2': -2,
#     '-3': -3,'-4': -4, 'skull': -int(input('Count of ghouls at your location? ')), 
#     'cultist': -1, 'tablet': -2, 'Elder_Sign': 1, 'auto_fail': -99
# }
#список с ключами от словаря
night_of_the_zealot_normal_bag_keys = ['+1', '0', '0', '-1', '-1', '-1', '-2', '-2', '-3', '-4', 
    'skull', 'skull', 'cultist', 'tablet', 'Elder_Sign', 'auto_fail']

#для тестов
only_auto_fail_bag = {'auto_fail': -99}
only_auto_fail_bag_keys = ['auto_fail']
only_Elder_Sign_bag = {'Elder_Sign': 1}
only_Elder_Sign_bag_keys = ['Elder_Sign']

#print(night_of_the_zealot_normal_bag)

#def night_of_the_zealot_normal():
#    skull = -int(input('Count of ghouls at your location? '))
#    cultist = -1
#    tablet = -2
#    auto_fail = -99
#    Elder_Sign = 1
#    return [
#    1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull, skull, cultist, tablet, Elder_Sign, auto_fail
#    ]

def the_midnigth_masks_normal():
    skull = -int(input('The highest number of doom on a Cultist enemy in play? '))
    cultist = -2
    tablet = -3
    auto_fail = -99
    Elder_Sign = 1
    return [
    1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull, skull, cultist, tablet, Elder_Sign, auto_fail
    ]

def the_devourer_below_normal():
    skull = -int(input('The number of Monster enemies in play? '))
    cultist = -2
    tablet = -3
    Elder_Thing = -5
    auto_fail = -99
    Elder_Sign = 1
    return [
    1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull, skull, cultist, tablet, Elder_Thing, Elder_Sign, auto_fail
    ]


#print(the_devourer_below_normal())

def main():
    if __name__ == '__main__':
        main()