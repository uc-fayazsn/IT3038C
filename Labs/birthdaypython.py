
print ("Please enter your birthday ")                                 #user input
yearOfBirth=int(input("Year:"))                                       #birth year
monthOfBirth=int(input("Month (1-12):"))                              #birth month
dayOfBirth=int(input("Day:"))                                         #birth date

from datetime import datetime                                         #import time 
now = datetime.now()
age = datetime(int(yearOfBirth), int(monthOfBirth), int(dayOfBirth))  #initialize birthday
calculation = now - age                                               #difference between now and birthday
print ("Your age is %d days " % (calculation.days))                   #calculation in days
print ("your age is %f seconds" % (calculation.seconds))              #calculation in seconds