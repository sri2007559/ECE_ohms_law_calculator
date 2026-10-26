print("OHM'S LAW CALCULATOR")
print("--------------------")

print("1. Calculate Voltage")
print("2. Calculate Current")
print("3. Calculate Resistance")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    current = float(input("Enter current in amperes: "))
    resistance = float(input("Enter resistance in ohms: "))
    voltage = current * resistance
    print("Voltage =", voltage, "V")

elif choice == "2":
    voltage = float(input("Enter voltage in volts: "))
    resistance = float(input("Enter resistance in ohms: "))
    if resistance != 0:
        current = voltage / resistance
        print("Current =", current, "A")
    else:
        print("Resistance cannot be zero.")

elif choice == "3":
    voltage = float(input("Enter voltage in volts: "))
    current = float(input("Enter current in amperes: "))
    if current != 0:
        resistance = voltage / current
        print("Resistance =", resistance, "ohms")
    else:
        print("Current cannot be zero.")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
