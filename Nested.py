print("===Welcome to Rider Builder===")
print("Step 1 \n1.Bike \n2.Car")
choice=int(input("Chose 1 or 2 "))
if choice == 1:
    print("Step 2 \nPick your bike type \n1.Scoter \n2Mountain bike")
    bike_type =int(input("Chose 1 or 2 "))
    if bike_type == 1:
        print("You Picked the Scoter")
        print("Speed  :39km/h ")
        print("Best for  :City roads")
    else:
        print("You Picked the Mountain bike")  
        print("Speed  :189km/h")
        print("Best for  :Mountain roads")  
elif choice == 2:
    print("Step 2 \nPick your Car type \n1.Sedan \n2SUV")
    Car_type =int(input("Chose 1 or 2 "))
    if Car_type == 1:
            print("You Picked the Sedan")
            print("Seats :5 Seats ")
            print("Best for  :Famliy trips")
    else:
            print("You Picked the SUV")  
            print("Seats :7 Seats ")
            print("Best for  :Adventure trips")  

else:
     print("invaild Choice")

print("=== Your Custom Ride is Ready ===")