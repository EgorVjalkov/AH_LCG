#night_of_the_zealot_normal_bag = [
#    1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 'skull', 'skull', 'cultist', 'tablet', 'Elder_Sign', 'auto_fail'
#    ]

def night_of_the_zealot_normal():
    skull = -int(input('Count of ghouls at your location? '))
    cultist = -99
    tablet = -99
    auto_fail = -99
    Elder_Sign = -99
    return [
    1, 0, 0, -1, -1, -1, -2, -2, -3, -4, skull, skull, cultist, tablet, Elder_Sign, auto_fail
    ]

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