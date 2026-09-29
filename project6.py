def main():
    print("*" * 50)
    print("UTTAR PRADESH POWER CORPORATION LIMITED")
    print("Bill of Supply for Electricity")
    print("*" * 50)

    # Input section with basic validation
    name = input("Customer Name: ").strip()
    number = input("Customer Number: ").strip()

    while True:
        try:
            old = int(input("Old Meter Reading: "))
            current = int(input("Current Meter Reading: "))
            
            if current < old:
                print("Error: Current reading cannot be less than old reading.\n")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.\n")

    # Electricity Charge Calculation
    units = current - old

    if units <= 100:
        charge = units * 3.25
    else:
        charge = (100 * 3.25) + ((units - 100) * 4.75)

    fixed = 250.0
    tax = charge * 0.115
    total = charge + fixed + tax

    # Display Output / Invoice
    print("\n" + "=" * 50)
    print(f"Customer Name        : {name}")
    print(f"Customer Number      : {number}")
    print(f"Old Meter Reading    : {old}")
    print(f"Current Meter Reading: {current}")
    print(f"Total Units Consumed : {units}")
    print("-" * 50)
    print(f"Fixed Rental Charge  : ₹{fixed:.2f}")
    print(f"Total Units Charge   : ₹{charge:.2f}")
    print(f"Total Tax (11.5%)    : ₹{tax:.2f}")
    print("-" * 50)
    print(f"Total Bill Payable   : ₹{total:.2f}")
    print("*" * 50)

if __name__ == "__main__":
    main() 