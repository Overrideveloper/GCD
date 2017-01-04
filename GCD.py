#Owner: Overrideveloper
#Description: GCD Program 

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
