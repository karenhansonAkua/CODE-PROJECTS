
# question 1

# Get coefficients a, b, and c from user input
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Display the result based on the discriminant value
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"The roots are {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The root is {root}")
else:
    print("The equation has no real roots.")