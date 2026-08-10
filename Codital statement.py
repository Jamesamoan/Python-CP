temperature = int(input("Enter today's temperature in Celisius:"))

if temperature < 20:
    outfit="jacket"
    print("its is cold today.")
    print("Wear a ", outfit)
else:
    outfit = "t_shirt"
    print("It is  warm today")
    print("Wear a", outfit)

is_raining=input("Is it raining today? (yes/no)")

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h:"))

if wind_speed>30:
    needs_windbraker = "yes"
    print("It is windy today.")
    print("Wear a windbraker over your", outfit)
else:
    needs_windbraker="no"
    print("It is clam today.")
    print("No windbreaker needed over your", outfit)

has_puddlles=input("Are there puddles on the ground? (yes/no)")

if has_puddlles == "yes":
    shoes="boots"
    print("The ground is wet.")
    print("Wear",shoes)
else:
    shoes="sneakers"
    print("The ground is wet")
    print("Wear", shoes)

print("")
print("Weather cheak complete!")

print("=====Weather Outfit Picker=====")
print("Temperture",temperature)
print("Outfit",outfit)
print("Raining",is_raining)
print("Wind Speed",wind_speed)
print("Shoes",shoes)
