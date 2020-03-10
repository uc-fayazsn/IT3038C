import time
def updateLog():

    print('''
    
    Welcome to Fayaz's IT3038C Calculator. For Project 2 the updates to this code include expotentials, remainder, and modulus functionalities as well as a way to calculation using the calculator outside of running the program. Division functions now restart the calculator with a message if the denominator is equal to 0, as this an error. The calculator will start shortly. Enjoy!
    
    ''')

def calculate():

    operation = input('''

Please type in the math operation you would like to complete:

+ for addition

- for subtraction

* for multiplication

/ for division

** for exponents

% for remainder

// for floor division

''')



    inputOne = int(input('Please enter the first number: '))

    inputTwo = int(input('Please enter the second number: '))



    if operation == '+':

        print('{} + {} = '.format(inputOne, inputTwo))

        print(inputOne + inputTwo)



    elif operation == '-':

        print('{} - {} = '.format(inputOne, inputTwo))

        print(inputOne - inputTwo)



    elif operation == '*':

        print('{} * {} = '.format(inputOne, inputTwo))

        print(inputOne * inputTwo)



    elif operation == '/':
       while inputTwo != 0:
        
        print('{} / {} = '.format(inputOne, inputTwo))

        print(inputOne / inputTwo)
        onemoretime()
       else:
       
        print('You have a zero in the denominator, please restart calculations as this value is undefined. ')
        time.sleep(2)
        
        

    elif operation == '**':
      
      print('{} ** {} = '.format(inputOne, inputTwo))

      print(inputOne ** inputTwo)
      
    
    elif operation == '%':
      
      print('{} % {} = '.format(inputOne, inputTwo))

      print(inputOne % inputTwo) 
      
    elif operation == '//':
      while inputTwo != 0:
        
        print('{} / {} = '.format(inputOne, inputTwo))

        print(inputOne / inputTwo)
        onemoretime()
      else:
        print('You have a zero in the denominator, please restart calculations as this value is undefined. ')
        time.sleep(2)

    else:

        print('You have not typed a valid operator, please run the program again.')



    # Add onemoretime() function to calculate() function

    onemoretime()



def onemoretime():

    calc_onemoretime = input('''

Do you want to calculate another time?

Please type Y for YES or N for NO.

''')



    if calc_onemoretime.upper() == 'Y':

        calculate()

    elif calc_onemoretime.upper() == 'N':

        print('See you later. Thank you for using this calculator.')

    else:

        onemoretime()


updateLog()
time.sleep(2)
calculate()