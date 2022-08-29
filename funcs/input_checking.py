def input_checking(question, checking=('y', 'n')):
    while True:
        value = input(question)
        if checking == 'num':
            if value.isdigit():
                break
        if checking == 'l':
            if value.isalpha():
                break
        if type(checking) == tuple:
            if value in checking:
                break
        print('Input error!')
#        print(question)
    return value

def main():
    if __name__ == '__main__':
        print(input_checking('enter a letter ', 'l'))

main()
