print("Welcome to the unit converter system!")

# Function for length conversions
def convert_length():
    print("1. Meter to kilometers")
    print("2. Kilometers to meters")
    print("3. Miles to kilometers")
    print("4. Kilometers to miles")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Meter to kilometer conversion:")
        meter = int(input("Enter the value: "))
        print(f"{meter} meter is equal to: {meter / 1000} kilometers")
    elif choice == 2:
        print("Kilometer to meter conversion:")
        kilometer = int(input("Enter the value: "))
        print(f"{kilometer} kilometer is equal to: {kilometer * 1000} meters")
    elif choice == 3:
        print("Miles to kilometers conversion:")
        miles = int(input("Enter the value: "))
        print(f"{miles} miles is equal to: {miles * 1.609} kilometers")
    elif choice == 4:
        print("Kilometers to miles conversion:")
        kilometer = int(input("Enter the value: "))
        print(f"{kilometer} kilometer is equal to: {0.62137119 * kilometer} miles")
    else:
        print("Enter a valid choice, please.")

# Function for temperature conversions
def convert_temperature():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Fahrenheit to Kelvin")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Celsius to Fahrenheit:")
        celsius = float(input("Enter the value: "))
        print(f"{celsius} Celsius is equal to: {(9/5)*celsius + 32} Fahrenheit")
    elif choice == 2:
        print("Fahrenheit to Celsius:")
        fahrenheit = float(input("Enter the value: "))
        print(f"{fahrenheit} Fahrenheit is equal to: {(5/9)*(fahrenheit - 32)} Celsius")
    elif choice == 3:
        print("Celsius to Kelvin:")
        celsius = float(input("Enter the value: "))
        print(f"{celsius} Celsius is equal to: {celsius + 273.15} Kelvin")
    elif choice == 4:
        print("Fahrenheit to Kelvin:")
        fahrenheit = float(input("Enter the value: "))
        print(f"{fahrenheit} Fahrenheit is equal to: {((fahrenheit - 32) * 5/9) + 273.15} Kelvin")
    else:
        print("Enter a valid choice, please.")

# Main function that runs the program
def main():
    while True:
        print("\nMain Menu:")
        print("1. Length Conversion")
        print("2. Temperature Conversion")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            convert_length()
        elif choice == 2:
            convert_temperature()
        elif choice == 3:
            print("Thank you for using the Unit Converter!")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the main function
if __name__ == "__main__":
    main()

#similarly we can add more uni converter like these two 