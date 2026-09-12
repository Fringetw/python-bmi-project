#BMI計算器
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("體重和身高必須大於0")
    return weight / (height ** 2)

#分類BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "體重正常"
    elif bmi < 27:
        return "體重過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

#計算正常體重範圍
def normal_weight_range(height):
    min_weight = 18.5 * (height ** 2)
    max_weight = 24 * (height ** 2)
    return min_weight, max_weight

# 顯示 BMI 分類的簡單說明
def bmi_message(bmi):
    if bmi < 18.5:
        return "你的 BMI 低於正常範圍。"
    elif bmi < 24:
        return "你的 BMI 位於正常範圍。"
    elif bmi < 27:
        return "你的 BMI 高於正常範圍。"
    elif bmi < 30:
        return "你的 BMI 為輕度肥胖範圍。"
    elif bmi < 35:
        return "你的 BMI 為中度肥胖範圍。"
    else:
        return "你的 BMI 為重度肥胖範圍。"

# 計算與正常體重範圍的差距
def weight_difference(weight, height):
    min_weight, max_weight = normal_weight_range(height)

    if weight < min_weight:
        return f"距離正常體重下限還差 {min_weight - weight:.1f} kg"
    elif weight > max_weight:
        return f"比正常體重上限多 {weight - max_weight:.1f} kg"
    else:
        return "目前位於正常體重範圍內"