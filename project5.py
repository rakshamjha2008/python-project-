print("🍕 Welcome to Python Pizza Hut!")

# Pizza size
size = input("What size of pizza do you want? Small (S), Medium (M), or Large (L): ").upper()

# Pizza price
if size == "S":
    bill = 150
elif size == "M":
    bill = 200
elif size == "L":
    bill = 250
else:
    print("Invalid pizza size!")
    exit()

# Add-ons
cheese = input("Do you want extra cheese? (Rs.30) Y or N: ").upper()
onion = input("Do you want extra onion? (Rs.20) Y or N: ").upper()
tomato = input("Do you want extra tomato? (Rs.30) Y or N: ").upper()
capsicum = input("Do you want extra capsicum? (Rs.30) Y or N: ").upper()
corn = input("Do you want extra corn? (Rs.20) Y or N: ").upper()

# Calculate add-on prices
if cheese == "Y":
    bill += 30

if onion == "Y":
    bill += 20

if tomato == "Y":
    bill += 30

if capsicum == "Y":
    bill += 30

if corn == "Y":
    bill += 20

# Final bill
print("--------------------------------")
print("Your final bill is: Rs.", bill)