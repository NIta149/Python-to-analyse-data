
#Write a Python program to get the Python version you are using.  
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


#Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Write a Python program which accepts the radius of a circle from the user and compute the area. 
 Sample Output :
r = 1.1
Area = 3.8013271108436504
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them 
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
