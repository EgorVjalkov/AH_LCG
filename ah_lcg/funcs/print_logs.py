from ah_lcg.funcs.colored_keywords import names_in_color


# НЕОБХОДИМО СДЕЛАТЬ ПОИСК ПО ЛОГАМ (НЕ ПОНИМАЮ КАК КУРСОР ДВИГАТЬ)

# при попытке открыть логи из файла, а не из терминала через поэтри
try:
    logs = open('ah_lcg/logs/logs.txt')
except FileNotFoundError:
    logs = open('../logs/logs.txt')


def print_logs(count_of_last_logs=0):
    if count_of_last_logs > 0:
        cursor1 = logs.tell()
        print(cursor1)
        logs.seek(10, 1)
        cursor2 = logs.tell()
        print(cursor2)
        for_print = logs.read()
    else:
        for_print = logs.read()
    print(names_in_color(for_print))


def main():
    print_logs()


main()
