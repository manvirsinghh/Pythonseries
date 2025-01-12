import math
import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check for real or complex solutions
    if discriminant >= 0:
        # Real solutions
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return (root1, root2)
    else:
        # Complex solutions
        sqrt_discriminant = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return (root1, root2)

def main():
    print("Solve a quadratic equation of the form ax^2 + bx + c = 0")

    # Input coefficients a, b, c
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a == 0:
        print("The coefficient 'a' cannot be zero for a quadratic equation.")
        return
    
    # Solve the quadratic equation
    root1, root2 = solve_quadratic(a, b, c)

    # Output the solutions
    print("\nSolutions:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

if __name__ == "__main__":
    main()
