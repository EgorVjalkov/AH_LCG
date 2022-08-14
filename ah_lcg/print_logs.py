from ah_lcg.game_data.colored_keywords import names_in_color


logs = open('ah_lcg/logs/logs.txt')
for_print = logs.read()
print(names_in_color(for_print))


def main():
    pass


main()
