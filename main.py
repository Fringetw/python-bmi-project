#BMI計算器
from bmi import (
    calculate_bmi,
    bmi_category,
    normal_weight_range,
    bmi_message,
    weight_difference, 
)

while True:
    print("\n===== BMI 測量程式 =====")

    try:
        height_cm = float(input("請輸入你的身高(cm): "))
        weight = float(input("請輸入你的體重(kg): "))

        height_m = height_cm / 100

        bmi = calculate_bmi(weight, height_m)       
        category = bmi_category(bmi)    

        min_weight, max_weight = normal_weight_range(height_m)

        print("\n===== 測量結果 =====")
        print(f"身高: {height_cm:.1f} cm")
        print(f"體重: {weight:.1f} kg")
        print(f"BMI: {bmi:.2f}")
        print(f"分類: {category}")

        print(f"說明: {bmi_message(bmi)}")

        print(
            f"此身高的正常體重範圍約為 "
            f"{min_weight:.1f} ~ {max_weight:.1f} kg"
        )
        print(weight_difference(weight, height_m))

    except ValueError:
        print("輸入錯誤，請輸入大於 0 的數字。")
        continue

    again = input("\n是否要再次測量？(y/n): ")

    if again.lower() != "y":
        print("BMI 測量程式結束")
        break