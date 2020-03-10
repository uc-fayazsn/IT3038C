This calculator is given two values input by the user and then applies whichever functionality of their choosing.

How to run this calculator: If you have python installed you can just double click the calc.py file and it will open up the cmd window with the update message and then prompt for which type of function you would like to choose. You can otherwise go to the path after you have cloned it in cmd

cd C:\~whereeveryouplacedit\
$ python calc.py

will run the file in the cmdline interface.



The types of functions are:

What the calculator calls for when it is looking for the function

'+ for addition

'- for subtraction

'* for multiplication

'/ for division

'** for exponentials

'% for remainder/modulus

'// for floor division



How the functions work


Addition will add the two inputs together (inputOne + inputTwo)

Subtractions will subtract the two inputs (inputOne - inputTwo)

Multiplcation will multiply the two inputs (inputOne * inputTwo)

Division will divide the two inputs. (inputOne / inputTwo)

Exponentials will perform their exponentials with the two inputs (inputOne ** inputTwo)

Modulus will provide the remainder of the two functions (inputOne % inputTwo)

Floor Division returns the integral part of the division (inputOne // inputTwo)



#division functions
the division functions have an error reporting if the second value (denominator) is a zero as the value is then undefined.

#import time
Time has been imported to allow the sleep function to occur after the welcome message and before the calculations begin.


#updateLog
Welcome message with a log of whats been added since project 1 was turned in.
