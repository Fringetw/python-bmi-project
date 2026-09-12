from bmi import calculate_bmi, bmi_category

weight = float(input("請輸入你的體重(kg): "))
height = float(input("請輸入你的身高(m): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"BMI: {bmi:.2f}")
print(f"分類: {category}")
