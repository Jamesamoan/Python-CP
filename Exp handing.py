#Write a program to understand how the value error exception works?
try:
    num=int(input("Enter a number: "))
    print(num)
except ValueError as es:
    print("Exception:",es)


#Write a program to check how the exceptions and finally statement works
try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError as De:
    print("Division by zero is error!!")
except ValueError as ve:
    print("Enter a valid number")
except:
    print("Wrong Input")
else:
    print("No Exceptions")
finally:
    print("This will execute no matter what")


#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.

valid = False
while not valid:
    try:
        num4=int(input("Enter a number: "))

        while num4%2==0:
            print("Bye")
        valid=True
    except ValueError:
        print("Invalid")
