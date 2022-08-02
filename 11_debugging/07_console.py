import code


def spam():
    eggs = 123
    print('The begin of spam')
    code.interact(banner='', local=locals())
    print('The end of spam')
    print(f'The value of eggs: {eggs}')


if __name__ == '__main__':
    spam()

