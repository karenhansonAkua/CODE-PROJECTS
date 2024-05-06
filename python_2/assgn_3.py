# Get systolic and diastolic blood pressure from user input
systolic = int(input("Enter systolic blood pressure: "))
diastolic = int(input("Enter diastolic blood pressure: "))

# Check blood pressure status
if systolic >= 140 or diastolic >= 90:
    print("High blood pressure")
elif systolic < 90 or diastolic < 60:
    print("Low blood pressure")
elif systolic >= 90 and systolic < 120 and diastolic >= 60 and diastolic < 80:
    print("Ideal blood pressure")
else:
    print("Invalid blood pressure value")