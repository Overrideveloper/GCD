#Owner: Overrideveloper
#Description: GCD Program 

from memory_profiler import memory_usage
from datetime import datetime
startTime = datetime.now()

#Creating a function that uses two parameters 
def GreatestCommonDivisor(x, y):

   while(y):
       x, y = y, x % y

   return x

#Taking user input 
FirstNumber = int(input("Enter the first number: /n"))

SecondNumber = int(input("Enter the second number: /n"))

ThirdNumber = int(input("Enter the third number: /n"))

FourthNumber = int(input("Enter the fourth number: /n"))

FifthNumber = int(input("Enter the fifth number: /n"))


output = GreatestCommonDivisor (GreatestCommonDivisor (GreatestCommonDivisor(GreatestCommonDivisor(FirstNumber,SecondNumber ),ThirdNumber),FourthNumber),FifthNumber)

print ("The Greatest Common Divisor of the five numbers is: ")

print (output)

print ("The execution time is ",(datetime.now()- startTime))

mem_usage = memory_usage(GreatestCommonDivisor)

print('Memory usage (in chunks of .1 seconds): %s'% mem_usage)

print('Maximum memory usage: %s'% max(mem_usage))
