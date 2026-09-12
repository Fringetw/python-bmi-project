from bmi import calculate_bmi

weight = float(input("請輸入你的體重(kg): "))
height = float(input("請輸入你的身高(m): "))

bmi = calculate_bmi(weight, height)

print(f"BMI: {bmi:.2f}")