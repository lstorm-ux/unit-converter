input("Hello! Welcome to Kilometers to Miles Converter!")

# Input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac

print('%0.2f kilometers is equal to %0.2f miles.' %(kilometers,miles))

# another conversion
while True:
    choice = input("Do you want to make another conversion?")

    if choice == "yes":
        kilometers = float(input("Enter value in kilometers: "))
        print('%0.2f kilometers is equal to %0.2f miles.' % (kilometers, miles))

    else:
        print("Goodbay, have a great day!")
        break




