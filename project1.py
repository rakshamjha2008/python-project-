maths = float(input("Enter maths marks: "))
science = float(input("Enter science marks: "))
sst = float(input("Enter SST marks: "))
hindi = float(input("Enter Hindi marks: "))
english = float(input("Enter English marks: "))

total = maths + science + sst + hindi + english

average = total / 5
percentage = (total / 500) * 100

print("Total marks:", total)
print("Average marks:", average)
print("Percentage:", percentage, "%")


