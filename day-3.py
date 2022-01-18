def setsTest():
    # Sets
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)

    print('orange in basket?', 'orange' in basket)

    print('crabgrass in basket?', 'crabgrass' in basket)

    a = set('abracadabra')
    b = set('alacazam')

    # unique letters in a
    print('unique letters in a\n', a)

    # letters in a but not in b
    print('letters in a but not in b (a-b)\n', a-b)

    # letters in a or b or both
    print('letters in a or b or both (a|b)\n', a|b)

    # letters in both a and b
    print('letters in both a and b (a&b)\n', a&b)

    # letters in a or b but not both
    print('letters in a or b but not both (a^b)\n', a^b)


    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print(tel)

    del tel['sape']
    tel['irv'] = 4127
    print(tel)

    print(list(tel))
    print(sorted(tel))


def formatTest():
    year = 2016
    event = 'Referendum'
    print(f'Results of the {year} {event}')

    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

setsTest()
formatTest()