# Project 3: Calculate Body Mass Index (BMI)

height_cm = float(input("Enter the height in cm: "))
weight_kg = float(input("Enter the weight in kg: "))

# Convert height from cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Display BMI
print("Your BMI is:", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")