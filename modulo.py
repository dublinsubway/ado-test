def main():
    name = str(input("What's your name?"))
    print('Hi {}, good to see you today!'.format(name))
    first = int(input('Please enter an integer you want to divide'))
    second = int(input('Please enter an integer you want to be divided by'))
    print('The result is {}, goodbye!'.format(modulo(first, second)))

def modulo(first, second):
    return int(first % second)

if __name__ == '__main__':
    main()