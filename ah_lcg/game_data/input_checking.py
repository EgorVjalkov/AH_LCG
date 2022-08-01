def input_checking(question, checking=('y', 'n')):
    while True:
        value = input(question)
        if checking == 'num':
            if value.isdigit():
                value = int(value)
                break
        if type(checking) == tuple:
            if value in checking:
                break
        print('Input error!')
#        print(question)
    return value

def main():
    if __name__ == '__main__':
        print(input_checking('enter a num ', (1,2,3,4,5)))

main()