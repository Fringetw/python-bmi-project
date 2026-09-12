def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "體重正常"
    elif bmi < 27:
        return "體重過重"
    else:
        return "肥胖"