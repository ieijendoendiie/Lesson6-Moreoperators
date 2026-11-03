height = float(input("Enter your height in (cm): "))
weight = float(input("Enter your weight in (kg): "))

Bmi = weight / (height/100)**2
if Bmi <=19.99:
    print("Underweight")
elif Bmi <=24.99:
    print("Healthy")
elif Bmi <=29.99:
    print("Litle Overweight")
elif Bmi <=34.99:
    print("Overweight")
elif Bmi <=39.99:
    print("Obese")
else:
    print("Too obese")
