def cal_bmi(weight_kg, height_m):

    bmi = weight_kg / (height_m ** 2)
    return bmi


def check_bmi(bmi):

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():

    weight = float(input("Enter your weight in kilograms: "))

    height = float(input("Enter your height in meters: "))

    bmi = cal_bmi(weight, height)

    interpretation = check_bmi(bmi)

    print("Your BMI is:", round(bmi, 2))
    print("Interpretation:", interpretation)


if __name__ == "__main__":
    main()
