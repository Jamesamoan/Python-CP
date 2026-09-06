#Write a program to demonstrate a right angle triangle pattern?
#print("==== Parttern ====")
#rows = int(input("Enter the numer of rows:" ))
#for i in range(rows):
#    for j in range (i+1):
 #        print("#", end=" ")
  #  print()

#rows = int(input("Enter the numer of rows:" ))
#number = 1
#for i in range(rows):
 #   for j in range (i+1):
  #       print(number, end=" ")
   #      number += 1
    #print()


rowSize = int(input("Enter the numer of rowSize:" ))
if rowSize%2==0:
    halfDimrow = int(rowSize/2)
else:
    halfDimrow = int(rowSize/2)+1
space=halfDimrow+1
for i in range(1, halfDimrow+1):
    for j in range(1 ,space+1):
        print(end= " ")
    space= space-1
    num = 1
    for j in range(2*i-1):
         print(end=str(num))
         num= num+1
    print()
space=1
for i in range(1,halfDimrow):
    for j in range(1, space+1):
        print(end= " ")
    space=space+1
    num = 1
    for j in range(1,2 *(halfDimrow-i)):
         print(end=str(num))
         num = num+1
    print()


    
    


