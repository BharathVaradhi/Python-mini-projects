def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return None, None

        return weight, height
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None

def main():
    print("=== BMI CALCULATOR ===")
    name = input("Enter your name: ")
    weight, height = get_user_input()

    if weight is not None and height is not None:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\n{name}, your BMI is: {bmi}")
        print(f"Health Category: {category}")

if __name__ == "__main__":
    main()
