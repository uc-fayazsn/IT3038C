def calculate():
    calculation = input('''
Please type in the math calculation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if calculation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif calculation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif calculation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif calculation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid entry, please use an operator listed in the above menu.')

    # Add continue() function to calculate() function
    continue()

def continue():
    calc_continue = input('''
Do you want to calculate continue?
Please type Y for YES or N for NO.
''')

    if calc_continue.upper() == 'Y':
        calculate()
    elif calc_continue.upper() == 'N':
        print('See you later.')
    else:
        continue()

calculate()