print("Welcome to the Game of Roller Coaster")

height = int(input("Enter the height of the person (in cm): "))
age = int(input("Enter the age of the person (in years): "))

if height < 100:
    print("Not eligible")
elif age <= 12:
    print("Ticket Price will be Rs. 50.")
elif age < 18:
    print("Ticket Price will be Rs. 70.")
elif age < 60:
    print("Ticket Price will be Rs. 100.")
else:
    print("Not eligible")

    